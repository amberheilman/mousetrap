# main gui running point

from gi.repository import Gtk
import button_gui_test
import cam_gui_test

class showGui(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self)
	
	def set_vars(self):
		cam = cam_gui_test.CameraWindow()
		buttons = button_gui_test.ButtonWindow()
		return cam, buttons

	def showCam(cam):
		runcam = cam.run()

	def showButtons(buttons):
		runbuttons = buttons.run()

	def start(self):
		startgui = showGui()
		startgui.set_vars()
		startgui.showCam()
		startgui.showButtons()

def main():
	Gtk.main()

if __name__ == '__main__':
	gui = showGui()
	gui.start()
