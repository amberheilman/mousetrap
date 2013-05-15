# MouseTrap GUI Rewrite
# main_2_test

import pygtk
pygtk.require('2.0')
import gtk
import dialogs_test
import settings_gui_test
import debug_test as debug
import environment_test as env
from addons import cpu_test

class MainGuiWindow(gtk.Window):

	def _show_settings_gui(self, *args):
		show_gui = settings_gui_test.PreffGui()
		show_gui.showPreffGui()
		return show_gui

	def _loadHelp(self, *args):
		try:
			import gnome
			gnome.help_display_uri("ghelp:%s/docs/mousetrap.xml" % env.mTDataDir)
		except ImportError:
			dialogs.errorDialog("mouseTrap needs <b>gnome</b> module to show the help. Please install gnome-python and try again.", None)
			debug.exception("mainGui", "The help load failed")

	def close(self, *args):
		gtk.main_quit()
	
	
	def delete_event(self, widget, event, data=None):
		gtk.main_quit()
		return False

	def __init__(self, controller):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.ctr = controller
		self.cfg = self.ctr.cfg
	
	def build_interface(self):
		self.window.set_title("MouseTrap")
		self.window.connect("delete_event", self.delete_event)
		self.window.set_border_width(200)

#		icon_theme = gtk.icon_theme_get_default()
#		try:
#			icon = icon_theme.load_icon("mousetrap", 48, 0)
#		except:
#			return
#		gtk.window_set_default_icon(icon)

#		self.setWindowsIcon()
		
#		accelGroup = gtk.AccelGroup()
#		self.window.add_accel_group(accelGroup)
#		self.accelGroup = accelGroup
		
		self.vBox = gtk.VBox()
		
		self.buttonsBox = gtk.HBox()
		
		self.prefButton = gtk.Button(stock=gtk.STOCK_PREFERENCES)
		self.prefButton.connect("clicked", self._show_settings_gui)
		self.vBox.pack_start(self.prefButton, True, True)
		
		self.closeButton = gtk.Button(stock=gtk.STOCK_QUIT)
		self.closeButton.connect("clicked", self.close)
		self.buttonsBox.pack_start(self.closeButton, True, True)
		
		self.helpButton = gtk.Button(stock=gtk.STOCK_HELP)
		self.helpButton.connect("clicked", self._loadHelp)
		self.buttonsBox.pack_start(self.helpButton, True, True)
		
		self.vBox.pack_start(self.buttonsBox, False, False)

#		self.adds_vbox = gtk.VBox()
#		self.adds_vbox.show_all()
#		self.vBox.pack_start(self.adds_vbox, False, False)

		self.statusbar = gtk.Statusbar()
		self.status_id = self.statusbar.get_context_id("statusbar")

		self.vBox.pack_start(self.statusbar, True, True)

		self.vBox.show_all()
		self.window.add(self.vBox)
		self.window.show()
	
def main():
	gtk.main()

if __name__ == '__main__':
	gui = MainGuiWindow()
	gui.build_interface()
	main()
