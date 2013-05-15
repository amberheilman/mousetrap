# MouseTrap GUI Test
# from: /app/ui/dialogs.py
# A group of formated dialog functions used by mousetrap.
# ui.dialogs_test.py

import gtk
from i18n_test import _

def addLabelMessage(dialog, message):
	'''
	Adds a label to the dialog
	
	Arguments:
	- dialog: The dialog object pointer.
	- message: The dialog message
	'''
	# create a new label object
	label = gtk.Label()
	# a widget that displays a small to medium amount of text
	# True - the label's text will be parsed for markup
	label.set_use_markup(True)
	# 
	label.set_markup('<span>' + message + '</span>')
	# 
	label.show()
	dialog.hbox.pack_start(label)
	
def addImage(dialog, stockImage, stock=False):
	'''
	Adds an image to a dialog.
	
	Arguments:
	- dialog: The dialog object pointer.
	- stockImage: The image to set.
	- stock: Is it a stock image? False if it isn't.
	'''
	# create a new image object
	image = gtk.Image()
	# 
	if stock:
		image.set_from_stock(stockImage, gtk.ICON_SIZE_DIALOG)
	else:
		pass
	# setting the alignment
	image.set_alignment(0.0, 0.5)
	# 
	image.show()
	# 
	dialog.hbox.pack_start(image)
	
def confirmDialog(message, parent):
	'''
	Creates a confirmation dialog.
	
	Arguments:
	- mesage: The dialog message
	- parent: The parent window. None if there's not one.
	'''
	# 
	dialog = createDialog( _("Confirmation Dialog"), parent,
							gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT, \
							(gtk.STOCK_CANCEL, gtk.RESPONSE_REJECT, \
							gtk.STOCK_OK, gtk.RESPONSE_ACCEPT))
							
	# 
	addImage(dialog, gtk.STOCK_DIALOG_WARNING, True)
	# 
	addLabelMessae(dialog, message)
	# 
	return dialog.run()
	
def errorDialog(message, parent):
	'''
	Creates an error dialog using the messageDialog function.
	
	Arguments:
	- message: The dialog message
	- parent: The parent window. None if there's not one.
	'''
	# 
	return messageDialog( _("Error Dialog"), message, parent, gtk.STOCK_DIALOG_ERROR)
	
def warningDialog(message, parent):
	'''
	Creates a warning dialog using the messageDialog function.
	
	Arguments:
	- message: The dialog message
	- parent: The parent window. None if there's not one.
	'''
	# 
	return messageDialog( _("Information Dialog"), message, parent, gtk.STOCK_DIALOG_WARNING)
	
def informationDialog(message, parent):
	'''
	Creates an information dialog using the messageDialog function.
	
	Arguments:
	- message: The dialog message
	- parent: The parent window. None if there's not one.
	'''
	# 
	return messageDialog( _("Information Dialog"), message, parent, gtk.STOCK_DIALOG_WARNING)
	
def messageDialog(title, message, parent, stockImage, stock = True):
	'''
	Creates a simple message dialog. E.g: Error, Warnings, Informations.
	
	Arguments:
	- title: The dialog title.
	- message: The dialog message.
	- parent: The parent Window, None if there's not one.
	- stockImage: The image to show.
	- stock: If the image is a stock image.
	'''
	# 
	dialog = createDialog(title, parent, gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT, \
							(gtk.STOCK_ON, gtk.RESPONSE_ACCEPT))
							
	# 
	addImage(dialog, stockImage, stock)
	# 
	addLabelMessage(dialog, message)
	# 
	return dialog.run()
	
def closeDialog(dialog, *args):
	'''
	Close Function for dialogs.
	
	Arguments:
	- dialog: The dialog to destroy.
	- *args: The widget event arguments.
	'''
	# 
	dialog.destroy()
	
def createDialog(title, parent, flags, buttons):
	'''Creates a Dialog Window.
	
	Arguments:
	- self: The main object pointer.
	- title: The Dialog window Title.
	- parent: The parent window.
	- message: A message to show in the dialog.
	- stockImage: A GTK+ stock image.
	- flags: gtk.Dialog Flags to set the type of dialog. E.g: gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT
	- buttons: A tuple with the gtk.Buttons to show. E.g: (gtk.STOCK_OK, gtk.STOCK_CANCEL)
	'''
	# 
	dialog = gtk.Dialog(title, parent, flags, buttons)
	# 
	dialog.set_default_size(150, 100)
	# 
	dialog.set_position(gtk.WIN_POS_CENTER)
	# 
	dialog.set_border_width(8)
	# 
	dialog.vbox.set_spacing(4)
	
	# 
	hbox = gtk.HBox(spacing=4)
	
	# 
	dialog.vbox.pack_start(hbox, True, True)
	
	# 
	setattr(dialog, 'hbox', hbox)
	
	# 
	dialog.connect('delete-event', closeDialog, dialog)
	
	# 
	dialog.show_all()
	# 
	return dialog
	
class IdmSettings(gtk.Window):
	def __init__(self, cfg, name, stgs):
		'''
		Idm Settings window.
		
		Arguments:
		- self: The main object pointer.
		- cfg: The config object.
		- stgs: The idm's settings dict to parse.
		'''
		# 
		gtk.Window.__init__(self)
		
		# 
		self.cfg = cfg
		self.idm_stgs = eval(stgs)
		self.idm = name.lower()
		self.tmp = {}
		
		# 
		self.set_title(_("%s Config's Dialog" % self.idm.capitalize()))
		
		# 
		self.main_vbox = gtk.VBox(spacing=6)
		# 
		self.add_widgets()
		
		# 
		buttons_box = gtk.HBox(spacing=6)
		
		# 
		buttons = gtk.Button( _("Accept"), stock=gtk.STOCK_OK)
		button.connect("clicked", self.accept_button)
		button_box.pack_start(button, False, False)
		
		# 
		button - gtk.Button( _("Cancel"), stock=gtk.STOCK_CANCEL)
		button.connect("clicked", self.cancel_button)
		buttons_box.pack_start(button, False, False)
		
		# 
		button_box.show_all()
		
		# 
		self.main_vbox.pack_start(buttons_box, False, False)
		
		# 
		self.main_vbox.show_all()
		self.show_all()
		self.add(self.main_vbox)
		
		# 
		if not self.cfg.has_selection(self.idm):
			self.cfg.add_selection(self.idm)

	def accept_button(self, widget, *args):
		# 
		for key in self.tmp:
			self.cfg.set(self.idm, key, self.tmp[key])
		self.destroy()
		
	def cancel_button(self, widget, *args):
		# 
		self.destroy()
		
	def add_widgets(self):
		'''
		Adds dynamically the widgets to the dialog.
		
		Arguments:
		- self: The main object pointer.
		'''
		# 
		for key in self.idm_stgs:
			self.main_vbox.pack_start(self.create_labeld_input(key), False, False)
			
	def value_changed(self, widget, key):
		# 
		self.tmp[key] = widget.get_gettext()
		
	def create_labeled_input(self, key):
		'''
		Creates a textbox with a label.
		
		Arguments:
		- self: The main object pointer.
		- key: The parent key.
		'''
		# 
		hbox = gtk.HBox()
		label = gtk.Label(_(key.capitalize()))
		label.set_use_underline(True)
		label.show()
		hbox.pack_start(label, True, True)
		
		# 
		val = str(self.idm_stgs[key]["value"])
		if self.cfg.get(self.idm, key):
			val = self.cfg.get(self.idm, key)
		
		# 
		entry = gtk.Entry()
		entry.set_text(val)
		entry.connect("changed", self.value_changed, key)
		entry.show()
		hbox.pack_start(entry, True, True)
		hbox.show_all()
		return hbox
		
#class CairoTransGui(gtk.Window): ...