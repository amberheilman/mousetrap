# Preferences GUI

from gi.repository import Gtk
#from original_gui_test.addons.handler_test import AddonsHandler

class PreffGui(Gtk.Window):
	def __init__(self):

		Gtk.Window.__init__(self, title="Preferences")

#		self.ctr = controller
#		self.cfg = self.ctr.cfg
#		self.adds = AddonsHandler(self.ctr)
#		self.preffWidgets = dict()

		self.accelgroup = Gtk.AccelGroup()
		self.add_accel_group(self.accelgroup)
		
#		self.connect("close", Gtk.main_close)
		self.set_deletable(True)

#		self.table = Gtk.Table(3, 6, False)

		self.notebook = Gtk.Notebook()
		self.notebook.set_tab_pos(Gtk.PositionType.TOP)
		self.notebook.set_show_tabs(True)
#		self.table.attach(self.notebook, 0, 6, 0, 1)
		self.add(self.notebook)
		self.notebook.show_all()

		self.main_gui_tab()
		self.cam_tab()
		self.algorithms_tab()
		self.addons_tab()
		self.mouse_tab()
		self.debug_tab()

		self.buttonbox = Gtk.HBox(False, spacing=6)

		self.acceptbutton = Gtk.Button(label="Accept")
		self.acceptbutton.connect("clicked", self.apply_clicked)
		self.buttonbox.pack_end(self.acceptbutton, True, True, 0)

		self.buttonbox.show_all()
#		self.table.attach(self.buttonbox, 0, 1, 2, 3, Gtk.AttachOptions.FILL, Gtk.AttachOptions.EXPAND)
#		self.add(self.buttonbox)
#		self.table.show_all()
#		self.add(self.table)
		self.show()

	def main_gui_tab(self):
		self.frame = Gtk.Frame()
		self.genbox = Gtk.VBox(spacing=6)

		self.camActive = Gtk.CheckButton(label="Activate camera module")
		self.genbox.pack_start(self.camActive, False, False, 0)

		self.flipImage = Gtk.CheckButton(label="Flip Image")
		self.genbox.pack_start(self.flipImage, False, False, 0)

		self.genbox.show_all()
		self.frame.add(self.genbox)
		self.frame.show()
		self.notebook.insert_page(self.frame, Gtk.Label("General"), 0)

	def cam_tab(self):
		self.frame = Gtk.Frame()
		self.cambox = Gtk.VBox(spacing=6)
		self.mapperActive = Gtk.CheckButton(label="Show Pointer Map")
		self.cambox.pack_start(self.mapperActive, False, False, 0)

		self.showCapture = Gtk.CheckButton(label="Show Capture")
		self.cambox.pack_start(self.showCapture, False, False, 0)

		self.cambox.show_all()
		self.frame.add(self.cambox)
		self.frame.show()
		self.notebook.append_page(self.frame, Gtk.Label("Camera"))

	def algorithms_tab(self):
		self.frame = Gtk.Frame()
		self.algobox = Gtk.VBox(spacing=6)
		self.confbutton = Gtk.Button(label="Algorithms Preferences")
		self.algobox.pack_start(self.confbutton, False, False, 0)
		self.algobox.show_all()
		self.frame.add(self.algobox)
		self.frame.show()
		self.notebook.append_page(self.frame, Gtk.Label("Addons"))

	def addons_tab(self):
		self.frame = Gtk.Frame()
		self.algobox = Gtk.VBox(spacing=6)
		self.confbutton = Gtk.Button(label="Addons Preferences")
		self.algobox.pack_start(self.confbutton, False, False, 0)
		self.algobox.show_all()
		self.frame.add(self.algobox)
		self.frame.show()
		self.notebook.append_page(self.frame, Gtk.Label("Addons"))

	def mouse_tab(self):
		self.frame = Gtk.Frame()
		self.cambox = Gtk.VBox(spacing=6)
		self.reqmov = Gtk.SpinButton()
		self.reqmov = Gtk.Label("Step Speed: ")
		self.cambox.pack_start(self.reqmov, False, False, 0)
		self.cambox.show_all()
		self.frame.add(self.cambox)
		self.frame.show()
		self.notebook.append_page(self.frame, Gtk.Label("Mouse"))

	def debug_tab(self):
		self.frame = Gtk.Frame()
		self.debugBox = Gtk.VBox(spacing=6)
		self.levelHbox = Gtk.HBox(spacing=4)
		self.levelLabel = Gtk.Label("Debugging Level: ")
		self.levelLabel.set_alignment(0.0, 0.5)
		self.levelLabel.show()
		self.levelHbox.pack_start(self.levelLabel, False, False, 0)
#		self.adj = Gtk.Adjustment(self.cfg.getint("main", "debugLevel", 10, 50, 10, 1, 0))
#		self.levelSpin = Gtk.SpinButton(self.adj, 0.0, 0)
#		self.levelSpin.set_wrap(True)
#		self.levelHbox.pack_start(self.levelSpin, False, False, 0)
		self.debugBox.pack_start(self.levelHbox, False, False, 0)
		self.debugBox.show_all()
		self.frame.add(self.debugBox)
		self.frame.show()
		self.notebook.append_page(self.frame, Gtk.Label("Debug"))

	def apply_clicked(self):
		print("You have clicked to apply changes")

def main():
	Gtk.main()

if __name__ == '__main__':
	pref = PreffGui()
	main()
