# example gtk program

import pygtk
pygtk.require('2.0')
import gtk

class gtk_sample:
  def callback(self, widget, data):
    print("Hello again - %s was pressed" % data)

  def delete_event(self, widget, event, data=None):
    gtk.main_quit()
    return False

  def __init__(self):
    self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    self.window.set_title("gtk example")
    self.window.connect("delete_event", self.delete_event)
    self.window.set_border_width(50)

    self.box1 = gtk.HBox(False, 0)
    self.window.add(self.box1)

    self.button1 = gtk.Button("Yes")
    self.button1.connect("clicked", self.callback, "yes")
    self.box1.pack_start(self.button1, True, True, 0)
    self.button1.show()

    self.button2 = gtk.Button("No")
    self.button2.connect("clicked", self.delete_event, "no")
    self.box1.pack_start(self.button2, True, True, 0)
    self.button2.show()

    self.box1.show()

    self.window.show()

def main():
  gtk.main()

if __name__ == '__main__':
  sample = gtk_sample()
  main()
