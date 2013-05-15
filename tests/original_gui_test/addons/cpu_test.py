# MouseTrap GUI Test
# from: /app/addons/cpu.py
# addons.cpu_test.py

import os # Misc. Operating System Interfaces
#from gi.repository import GObject # GLib Object System
import pygtk
pygtk.require('2.0')
import gobject

import sys
sys.path.append("../")
import debug_test as debug
import environment_test as env

from subprocess import Popen, PIPE # subprocess management
# Popen - ?
# PIPE - special value that can be used as the stdin, stdout, or stderr argument
# to Popen and indicates that a pipe to standard stream should be opened

from handler_test import AddonsBase # class from handler.py

a_name = "CPU"
a_description = "Checks the CPU % usage"
a_settings = {}

class Addon(AddonsBase):
	# 
	def __init__(self, controller):
		AddonsBase.__init__(self, controller)
		
		# sets the check_cpu function to be called at regular intervals
		# [interval, callback, ...(zero or more arguments passed to callback)]
		GObject.timeout_add(1000, self.check_cpu)
		debug.debug("addon.cpu", "CPU addon started")
	
	def check_cpu(self):
		'''
		Checks the cpu usage.
		
		Arguments:
		- self: The main object pointer.
		'''
		
		# script to check cpu usage
		cpu = (Popen("ps -e -o pcpu,pid | grep %s" % str(env.pid), shell=True, stdout=PIPE).stdout).read().strip().split(" ")[0]
		
		# write the message of the CPU usage to the status bar
		self.statusbar_message("CPU: %s" % cpu)
		return True
