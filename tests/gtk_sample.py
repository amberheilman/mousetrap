# example gtk program

import pygtk
pygtk.require('2.0')
import gtk

class gtk_sample:

  def callback(self, widget, data):
    """ 
     Function that tells a button what to do when clicked (?)
    """
    print("Hello again - %s was pressed" % data)

  def delete_event(self, widget, event, data=None):
    """ 
     The delete_event is one way of quitting the gui
    """ 
    gtk.main_quit()
    return False


  def __init__(self):
    """ 
     Builds the actual GUI window.
    """
    # Create the main window, setting the title, and 
    # connecting the "delete" event to the window. 
    self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    self.window.set_title("gtk example")
    self.window.connect("delete_event", self.delete_event)
    self.window.set_border_width(50)

    # Creates a box and is added to a window to make it visible. 
    # The "False"  ?? and 0 ??
    self.box1 = gtk.HBox(False, 0)
    self.window.add(self.box1)

    # Creates a button labeleed "Yes" that is connected to the callback event. 
    # Button is not visible yet.  
    self.button1 = gtk.Button("Yes")
    self.button1.connect("clicked", self.callback, "yes")
    # Button is potentially visible and will be visible 
    # when window becomes visible
    self.box1.pack_start(self.button1, True, True, 0)
    self.button1.show()

    # This creates a "No" button as above but connects it to 
    # the "delete_event" which closes the window.  
    self.button2 = gtk.Button("No")
    self.button2.connect("clicked", self.delete_event, "no")
    self.box1.pack_start(self.button2, True, True, 0)
    self.button2.show()

    # Makes box and window visible
    self.box1.show()
    self.window.show()

def main():
  gtk.main()

if __name__ == '__main__':
  sample = gtk_sample()
  main()
