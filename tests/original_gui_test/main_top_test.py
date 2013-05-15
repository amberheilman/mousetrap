# Top Main File Test

import sys
sys.argv[0] = "mousetrap"
sys.path.append("ui/")
sys.path.append("scripts/")
sys.path.append("addons/")

import pygtk
pygtk.require('2.0')
import gobject

import debug_test
#import getopt_test
import environment_test as env

from ocvfw import pocv_test

from i18n_test import _
from main_test import MainGui
from scripts_init_test import get_script_class

#from lib import httpd_test, dbusd_test, settings_test

class Controller():
	'''
	MouseTrap's Controller Class
	'''

	def __init__(self):
		'''
		The MouseTrap controller init class
		
		Arguments:
		- self: The main object pointer.
		'''

		self.cfg = None
		self.loop = GObject.MainLoop()
		self.httpd = httpd.HttpdServer(20433)
		self.dbusd = dbusd.DbusServer()

	def start(self):
		'''
		Starts the modules, views classes.
		
		Arguments:
		- self: The main object pointer.
		'''

		debug.debug("main", "in start")
		if self.cfg is None:
			conf_created, self.cfg = settings.load()

		self.proc_args()

		if not self.dbusd.start():
			self.httpd.start()

		if self.cfg.getboolean("main", "startCam"):
			idm = pocv.get_idm(self.cfg.get("main", "algorithm"))
			self.idm = idm.Module(self)
			self.idm.set_capture(self.cfg.getint("cam", "inputDevIndex"))
			GObject.timeout_add(150, self.update_frame)
			debug.debug("main", "Past update frame")
			GObject.timeout_add(50, self.update_pointers)

			debug.info("mousetrap", "Idm loaded and started")

		debug.debug("main", "Start building interface")
		self.itf = MainGui(self)
		self.itf.build_interface()
		self.itf.load_addons()

		if conf_created:
			from ui import settings_gui_test
			settings_gui_test.showPreffGui(self)


		debug.info("mousetrap", "MouseTrap's Interface Built and Loaded")
		GObject.threads_init()
		self.loop.run()

	def proc_args(self):
		'''
		Process the startup flags

		Arguments:
		- self: The main object pointer.
		'''

		arguments = sys.argv[1:]
		if len(arguements) == 1:
			arguments = arguments[0].split()

		env.flags = dict((key[0], {"section" : sec}) for sec in self.cfg.sections() for key in self.cfg.items(sec))

		try: 
			opts, args = getopt.getopt( arguments, "?hve:d:s",
			["help", "version", "enable=", "diable=", "set="])

			for opt, val in opts:
				key = False

				if opt in ("-s", "--set"):
					key, value = val.strip().split("-")

				if opt in("-e", "--enable"):
					key, value = [val.strip(), "True"]

				if opt in ("-d", "--disable"):
					key, value = [val.strip(), "False"]

				if key in env.flags:
					self.cfg.set(env.flags[key]["section"], key, value)
				elif key:
					self.usage()
					self.quit(2)

				if opt in ("-v", "--version"):
					print(env.version)
					self.quit(0)

				if opt in ("-?", "-h", "--help"):
					self.usage()
					self.quit(0)

		except getopt.GetoptError, err:
			print str(err)
			self.usage()
			self.quit(2)
			pass

	def usage(self):
		'''
		Prints the usage

		Agruments:
		- self: The main object pointer
		'''

		print( _("Usage: mouseTrap [OPTION...]"))

		print( "-?, -h, --help              " + \
			_("        Show this help message"))

		print ( "-s, --set            " + \
			_("               Sets new value to Non Boolean options E.g -s inputDevIndex-1"))

		print( "-e, --enable=[" + "main-window" + "|" + "cam" + "]")

		print( _("    Disable the selected options"))

		print( "-v, --version      " + \
			_("                 Shows mouseTrap version"))

		#print( _("\nReport bugs to flaper87@flaper87.org"))

	def script(self):
		'''
		Returns the main scripts class object.

		Arguments:
		- self: The main object pointer.
		'''

		return get_script_class(self.cfg.get("scripts", "name"))()

	def update_frame(self):
		'''
		Updates the User Interface frame with the latest capture.

		Arguments:
		- self: The main object pointer.
		'''

		debug.debug("main", "entered update_frame")
		self.itf.update_frame(self.idm.get_capture(), self.idm.get_pointer())
		debug.debug("main", "leaving update_frame")
		return True

	def update_pointers(self):
		'''
		Gets the new mouse pointer position based on the last calcs.

		Arguments:
		- self: The main object pointer.
		'''

		debug.debug("Main", "Entering update_pointers")
		self.itf.script.update_items(self.idm.get_pointer())
		return True

	def quit(self, exitcode=1):
		'''
		Quits mouseTrap and all its process

		Arguments:
		- self: The main object pointer.
		- exitcode: The exitcode number. It helps to handle some quit events.
		'''

		sys.exit(exitcode)
