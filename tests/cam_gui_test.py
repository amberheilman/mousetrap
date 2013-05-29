# MouseTrap Gtk3 Camera GUI
# cam_gui_test.py

import gi
gi.require_version("Gst", "1.0")
import sys, os
from gi.repository import Gtk, GObject, Gst
from gi.repository import GdkX11, GstVideo

GObject.threads_init()
Gst.init(None)

class CameraWindow(Gtk.Window):
	def __init__(self):
		self.window = Gtk.Window()
		self.window.set_title("MouseTrap")
		self.window.connect("destroy", self.quit)
		self.window.set_default_size(800, 450)
		self.window.set_position(Gtk.WindowPosition.CENTER)
		
		self.drawarea = Gtk.DrawingArea()
		self.window.add(self.drawarea)

		self.pipeline = Gst.Pipeline()

		self.bus = self.pipeline.get_bus()
		self.bus.add_signal_watch()
		self.bus.connect("message::error", self.on_error)

		self.bus.enable_sync_message_emission()
		self.bus.connect("sync-message::element", self.on_sync_message)

		self.src = Gst.ElementFactory.make("autovideosrc", None)
		self.sink = Gst.ElementFactory.make("autovideosink", None)

		self.pipeline.add(self.src)
		self.pipeline.add(self.sink)

		self.src.link(self.sink)

	def run(self):
		self.window.show_all()
		self.xid = self.drawarea.get_property('window').get_xid()
		self.pipeline.set_state(Gst.State.PLAYING)
		Gtk.main()

	def on_sync_message(self, bus, msg):
		if msg.get_structure().get_name() == "prepare-window-handle":
			print ("prepare-window-handle")
			msg.src.set_property("force-aspect-ratio", True)
			msg.src.set_window_handle(self.xid)

	def on_error(self, bus, msg):
		print ("on_error():", msg.parse_error())

	def quit(self, window):
		self.pipeline.set_state(Gst.State.NULL)
		Gtk.main_quit()

