# MouseTrap GUI Test
# from: /app/ui/main.py
# ui.main_test.py

import gtk # GIMPToolkit
import dialogs_test # file /app/ui/dialogs.py
import settings_gui_test # file /app/ui/settings_gui.py
import debug_test as debug # file /app/ui/dialogs.py
import environment_test as env # file /app/environment.py
from addons import cpu_test # file /app/addons/cpu.py

class MainGui(gtk.Window):
	'''
	MouseTrap Main GUI Class
	'''
	
	def __init__(self, controller):
		'''
		The main GUI constructor
		
		Arguments:
		- self: The main object pointer
		- controller: The mouseTrap's controller.
		'''
		
		gtk.Window.__init__(self)
		self.ctr = controller
		self.cfg = controller.cfg
		self.script = self.ctr.script()
		
	def setWindowsIcon(self):
		'''
		Sets the mainGui icon
		
		Arguments:
		- self: The main object pointer
		'''
		
		icon_theme = gtk.icon_theme_get_default()
		try:
			icon = icon_theme.load_icon("mousetrap", 48, 0)
		except:
			return
			
		gtk.window_set_default_icon(icon)
		
	def build_interface(self):
		'''
		Builds the interface
		
		Arguments:
		-self: The main object pointer
		'''
		
		self.setWindowsIcon()
		
		# gtk.AccelGroup - A group of accelerators for a Window hierarchy
		accelGroup = gtk.AccelGroup()
		self.add_accel_group(accelGroup)
		
		self.accelGroup = accelGroup
		
		# set the title of the window
		self.set_title("Mousetrap")
		# create an "exit" button
		self.connect("destory", self.close)
		self.setWindowsIcon()
		
		# create a vertical box to pack items in to
		self.vBox = gtk.VBox()
		
		# create a horizontal "buttons box"
		self.buttonsBox = gtk.HButtonBox()
		
		# create a "preferences" button with the default image,
		# attach en event to it, and pack it in to the buttonsBox
		self.prefButton = gtk.Button(stock=gtk.STOCK_PREFERENCES)
		self.prefButton.connect("clicked", self.__show__settings__gui)
		self.buttonsBox.pack_start(self.prefButton, True, True)
		
		# create a "close" button
		self.closeButton = gtk.Button(stock=gtk.STOCK_QUIT)
		self.closeButton.connect("clicked", self.close)
		self.buttonsBox.pack_start(self.closeButton, True, True)
		
		# create a "help" button
		self.helpButton = gtk.Button(stock=gtk.STOCK_HELP)
		self.helpButton.connect("clicked", self._loadHelp)
		self.buttonsBox.pack_start(self.buttonsBox, True, True)
		
		self.vBox.pack_start(self.buttonsBox, False, False)
		
		self.adds_vbox = gtk.VBox()
		self.adds_vbox.show_all()
		self.vBox.pack_start(self.adds_vbox, False, False)
		
		# gtk.Image - a widget displaying an image
		self.cap_image = gtk.Image()
		
		if self.cfg.getboolean("gui", "showCapture"):
			self.cap_expander = gtk.expander_new_with_mnemonic("_Camera Image")
			self.cap_expander.add(self.cap_image)
			self.cap_expander.set_expanded(True)
			self.vBox.pack_start(self.cap_expander)
			
		if self.cfg.getboolean("gui", "showPointerMapper"):
			self.map_expander = gtk.expander_new_with_mnemonic("_Script Mapper")
			self.map_expander.add(self.script)
			self.map_expander.set_expanded(True)
			self.vBox.pack_start(self.map_expander)
			
		self.statusbar = gtk.Statusbar()
		self.status_id = self.statusbar.get_context_id("statusbar")
		
		self.vBox.pack_start(self.statusbar, True, True)
		
		self.vBox.show_all()
		self.add(self.vBox)
		self.show()
		
		#debug.debug("ui.main", "Interface Built")
		
	# def load_addons...
	
	# def update_frame...
	
	# def _newStockImageButton...
	
	def _show_settings_gui(self, *args):
		'''
		Starts the preferences GUI
		
		Arguments:
		-self: The main object pointer.
		- *args: The widget callback arguments.
		'''
		settings_gui.showPreffGui(self.ctr)
		
	def _loadHelp(self, *args):
		'''
		Shows the user manual.
		
		Arguments:
		- self: The main object pointer.
		- *args: The widget callback arguments.
		'''
		try: 
			import gnome
			gnome.help_display_uri("ghelp:%s/docs/mousetrap.xml" % env.mTDataDir)
		except ImportError:
			dialogs.errorDialog(
			"mouseTrap needs <b>gnome</b> module to show the help. Please install gnome-python and try again.", None)
			debug.exception("mainGui", "The help load failed")
			
	def close(self, *args):
		'''
		Close Function for the quit button, This will kill mousetrap.
		
		Arguments:
		- self: The main object pointer.
		- *args:The widget callback arguments.
		'''
		self.str.quit(0)
		
def showMainGui():
	'''
	Loads the mainGUI components and launch it.
	
	Arguments:
	- mouseTrap: The mouseTrap object pointer.
	'''
	gui = MainGui()
	gui.build_interface()
	return gui
