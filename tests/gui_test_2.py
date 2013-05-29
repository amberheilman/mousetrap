# Second MouseTrap GUI test...

from gi.repository import Gtk
import cam_gui_test
import prefgui_test

class MainWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="Options")
		self.connect("delete-event", Gtk.main_quit)

		self.table = Gtk.Table(1, 3, True)
		self.add(self.table)

		self.prefbutton = Gtk.Button(label="Preferences")
		self.prefbutton.connect("clicked", self._pref)
		self.table.attach(self.prefbutton, 0, 1, 0, 1)

		self.quitbutton = Gtk.Button(label="Quit")
		self.quitbutton.connect("clicked", self._quit)
		self.table.attach(self.quitbutton, 1, 2, 0, 1)

		self.helpbutton = Gtk.Button(label="Help")
		self.helpbutton.connect("clicked", self._help)
		self.table.attach(self.helpbutton, 2, 3, 0, 1)

		self.table.show_all()

		#add webcam call here??
		cam = cam_gui_test.CameraWindow()

		self.show()
		cam.run()

	def _pref(self, widget):
		prefgui_test.PreffGui()

	def _quit(self, widget):
		Gtk.main_quit()

	def _help(self, widget):
		print ("You have clicked help")


def main():
	Gtk.main()

if __name__ == '__main__':
	win = MainWindow()
	Gtk.main()
