# MouseTrap GUI Test
# from: /app/ui/settings_gui.py
# ui.settings_gui_test.py

import gtk
import sys
sys.path.append('/home/MouseTrap/wne/tests/original_gui_test/ocvfw')
sys.path.append('/home/MouseTrap/wne/tests/original_gui_test')
sys.path.append('/home/MouseTrap/wne/tests/original_gui_test/scripts')
sys.path.append('/home/MouseTrap/wne/tests/original_gui_test/addons')
import dialogs_test
from i18n_test import _
import pocv_test
import environment_test as env

from scripts_init_test import get_scripts_list
from handler_test import AddonsHandler

class PreffGui(gtk.Window):
	'''
	The Class for the prefences GUI
	
	Arguments:
	- gtk.Window: The gtk.Window Object.
	'''
	
	def __init__(self, controller):
		'''
		The Class Constructor.
		
		Arugments:
		- self: The main object pointer.
		- mouseTrap: The mosueTrap object pointer.
		'''
		
		gtk.Window.__init__(self)
		
		self.ctr = controller
		self.cfg = self.ctr.cfg
		self.adds = AddonsHandler(self.ctr)
		self.preffWidgets = dict()
		
	def setWindowsIcon(self):
		'''
		Sets the icon for the preffGUI
		
		Arguments:
		- self: The main object pointer.
		'''
		# returns a unique gtk.IconTheme associated with
		# the default gtk.gdk.Screen. Can be used as long
		# as the screen is open
		icon_theme = gtk.icon_theme_get_default()
		# try to load the mouseTrap specific icon
		try:
			icon = icon_theme.load_icon("mouseTrap", 48, 0)
		except:
			return
		# set the default icon to "icon" from the
		# previous call
		gtk.window_set_default_icon(icon)
		
	def buildInterface(self):
		'''
		Builds the preffGUI.
		
		Arguments:
		- self: The main object pointer.
		'''
		# creates an AccelGroup object
		accelGroup = gtk.AccelGroup()
		self.add_accel_group(accelGroup)
		
		accelGroup = accelGroup
		
		# set title of the the window
		self.set_title( _("mouseTrap Preferences") )
		# sets the width, height in pixels
		self.set_size_request(600, 400)
		# "create" the exit button
		self.connect("destroy", self.close)
		
		# create a table object with [rows, columns, homogeneous]
		self.table = gtk.Table(3, 6, False)
		
		# create a note book object
		self.notebook = gtk.Notebook()
		# sets the edge at which the tabs for switching pages in
		# in the notebook are drawn - TOP here
		self.notebook.set_tab_pos(gtk.POS_TOP)
		# attach the notebook object to the table object
		# [child, left_attach, right_attach, top_attach, bottom_attach]
		self.table.attach(self.notebook, 0, 6, 0, 1)
		# show the notebook object
		self.notebook.show()
		
		# add the tabs formed below
		self.main_gui_tab()
		self.cam_tab()
		self.algorithm_tab()
		self.addons_tab()
		self.mouseTab()
		self.debug_tab()
		
		# create a horizontal button box
		# [homogeneous, spacing]
		self.buttonsBox = gtk.HBox(False, spacing=6)
		
		# create an "Accept" button and connect it to the "applyButtonClick" call
		# add it to the buttonsBox
		self.acceptButton = gtk.Button( _("Accept"), stock=gtk.STOCK_OK)
		self.acceptButton.connect("clicked", self.applyButtonClick)
		self.buttonsBox.pack_end(self.applyButton)
		
		self.buttonsBox.show_all()
		
		# [child, left_attach, right_attach, top_attach, bottom_attach,
		# xoptions, yoptions]
		self.table.attach(self.buttonsBox, 1, 2, 2, 3, 'fill', False)
		# show the table object
		self.table.show()
		# add the table object to the main pointer object
		self.add(self.table)
		# show the main pointer object
		self.show()
		
	def main_gui_tab(self):
		'''
		The mainGui Preff Tab.
		
		Arguments:
		- self: THe main object pointer.
		'''
		
		# create a frame object
		frame = gtk.Frame()
		
		# create a vertical box object
		general_box = gtk.VBox(spacing = 6)
		
		# create a checkButton object for setting the camera to active- [name]
		# set it to active and connect it to the "_checkToggled" call
		# pack it into the general_box - [child, expand, fill, padding]
		cAmActive = gtk.CheckButton( _("Activate Camera module") )
		cAmActive.set_active(self.cfg.getboolean("main", "startCAm"))
		cAmActive.connect("toggled", self._checkToggled, "main", "startCam")
		general_box.pack_start(cAmActive, False, False)
		
		# create a check button to flip the image on the screen
		flipImage = gtk.CheckButton( _("Flip Image") )
		flipImage.set_active(self.cfg.getboolean("cam", "flipImage"))
		flipImage.connect("toggled", self._checkToggled, "cam", "flipImage")
		
		# pack flip image into general_box
		general_box.pack_start(flipImage, False, False)
		
		# ?
		inputDevIndex = self.addSpin( _("Input Video Device Index: "), "inputDevIndex", self.cfg.getint("cam", "inputDevIndex"), "cam", "inputDevIndex", 0)
		general_box.pack_start(inputDevIndex, False, False)
		
		general_box.show_all()
		
		frame.add(general_box)
		frame.show()
		
		self.noteBook.insert_page(frame, gtk.Label( _("General") ) )
		
	def cam_tab(self):
		'''
		The cam module Preff Tab.
		
		Arguments:
		- self: The main object pointer.
		'''
		
		# create the cam_tab (like main_gui_tab)
		frame = gtk.Frame()
		
		camBox = gtk.VBox(spacing = 6)
		
		mapperActive = gtk.CheckButton( _("Show Point Mapper") )
		mapperActive.set_active(self.cfg.getboolean("gui", "showPointMapper") )
		mapperActive.connect("toggled", self._checkToggled, "gui", "showPointMapper")
		
		camBox.pack_start(mapperActive, False, False)
		
		showCapture = gtk.CheckButton( _("Show Capture") )
		showCapture.set_active(self.cfg.getboolean("gui", "showCapture"))
		showCapture.connect("toggled", self._checkToggled, "gui", "showCapture")
		
		camBox.pack_start(showCapture, False, False)
		
		camBox.show_all()
		
		frame.add(camBox)
		frame.show()
		
		self.noteBook.insert_page(frame, gtk.Label( _("Camera") ) )
		
	def algorithm_tab(self):
		'''
		The cam module Preff Tab.
		
		Arguments:
		- self: The main object pointer.
		'''
		# create the algorithm_tab
		frame = gtk.Frame()
		
		algo_box = gtk.VBox(spacing = 6)
		
		# 
		liststore = gtk.ListStore(bool, str, str, str)
		
		conf_button = gtk.Button(stock=gtk.STOCK_PREFERENCES)
		conf_button.connect('clicked', self.show_alg_pref, liststore)
		conf_button.set_sensitive(False)
		
		# 
		scripts_combo = gtk.combo_box_new_text()
		scripts_combo.append_text(self.cfg.get("scripts", "name"))
		
		# 
		for script in get_scripts_list():
			if script.lower() != self.cfg.get("scripts", "name"):
				scripts_combo.append_text(script)
		
		# 
		scripts_combo.connect('changed', self._comboChanged, "scripts", "name")
		scripts_combo.set_active(0)
		
		# 
		tree_view = gtk.TreeView(liststore)
		tree_view.connect("cursor-changed", self._tree_view_click, conf_button)
		
		# 
		toggle_cell = gtk.CellRendererToggle()
		toggle_cell.set_radio(True)
		toggle_cell.connect('toggled', self._toggle_cell_changed, liststore)
		toggle_cell.set_property('activatable', True)
		
		# 
		name_cell = gtk.CellRendererText()
		desc_cell = gtk.CellRendererText()
		
		# 
		toggle_column = gtk.TreeViewColumn(_('Active Algorithms'), toggle_cell)
		name_column = gtk.TreeViewColumn(_('Installed Algorithms'))
		desc_column = gtk.TreeViewColumn(_('Description'))
		
		# 
		for alg in pocv.get_idms_list():
			alg_inf = pocv.get_idm_inf(alf)
			
			if not alg_inf:
				continue
			
			state = Flase
			if alg_inf["name"].lower() in self.cfg.get("main", "algorithm").lower():
				state = True
			liststore.append([state, alg_inf("name"), alg_inf["dsc"], alg_inf["stgs"]])
		
		# 	
		tree_view.append_column(toggle_column)
		tree_view.append_column(name_column)
		tree_view.append_column(desc_column)
		
		# 
		name_column.pack_start(name_cell, True)
		desc_column.pack_start(desc_cell, True)
		
		# 
		toggle_column.add_attribute(toggle_cell, "active", 0)
		toggle_column.set_max_width(30)
		name_column.set_attributes(name_cell, text=1)
		desc_column.set_attributes(desc_cell, text=2)
		
		# 
		algo_box.pack_start(tree_view)
		algo_box.pack_start(conf_button, False, False)
		algo_box.pack_start(scripts_combo, False, False)
		
		# 
		algo_box.show_all()
		
		frame.add(algo_box)
		frame.show()
		
		self.noteBook.insert_page(frame, gtk.Label( _("Algorithm") ) )
		
	def addons_tab(self):
		'''
		The cam module for Preff Tab.
		
		Arguments:
		- self: The main object pointer.
		'''
		
		# create the addons_tab (like algorithm_tab)
		frame = gtk.Frame()

		algo_box = gtk.VBox( spacing = 6 )

		liststore = gtk.ListStore(bool, str, str, str)

		conf_button = gtk.Button(stock=gtk.STOCK_PREFERENCES)
		conf_button.connect('clicked', self.show_alg_pref, liststore)
		conf_button.set_sensitive(False)

		tree_view = gtk.TreeView(liststore)
		tree_view.connect("cursor-changed", self._tree_view_click, conf_button)

		toggle_cell = gtk.CellRendererToggle()
		toggle_cell.connect( 'toggled', self._enable_disable_addon, liststore)
		toggle_cell.set_property('activatable', True)

		name_cell = gtk.CellRendererText()
		desc_cell = gtk.CellRendererText()

		toggle_column = gtk.TreeViewColumn(_('Active'), toggle_cell)
		name_column = gtk.TreeViewColumn(_('Name'))
		desc_column = gtk.TreeViewColumn(_('Description'))

		for add in self.adds.get_addons_list():
		    add_inf = self.adds.get_addon_inf(add)
		    
		    if not add_inf:
			continue
		    
		    state = False
		    if add_inf["name"].lower() in self.cfg.getList("main", "addon"):
			state = True
		    liststore.append([state, add_inf["name"], add_inf["dsc"], add_inf["stgs"]])

		tree_view.append_column(toggle_column)
		tree_view.append_column(name_column)
		tree_view.append_column(desc_column)

		name_column.pack_start(name_cell, True)
		desc_column.pack_start(desc_cell, True)

		toggle_column.add_attribute( toggle_cell, "active", 0 )
		toggle_column.set_max_width(30)
		name_column.set_attributes(name_cell, text=1)
		desc_column.set_attributes(desc_cell, text=2)

		algo_box.pack_start(tree_view)
		algo_box.pack_start(conf_button, False, False)

		algo_box.show_all()

		frame.add( algo_box )
		frame.show()

		self.noteBook.insert_page(frame, gtk.Label( _("Addons") ) )

	def mouseTab(self):
		'''
		The cam module Preff Tab.
		
		Arguments:
		- self: The main object pointer.
		'''
		
		frame = gtk.Frame()
		
		camBox = gtk.VBox(spacing = 6)
		
		reqMov = self.addSpin( _("Step Speed: "), "stepSpeed", self.cfg.getint("mouse", "stepSpeed"), "mouse", "stepSpeed")
		camBox.pack_start(reqMov, False, False)
		
		camBox.show_all()
		
		frame.add(camBox)
		frame.show()
		
		# insert a page into the location (if specified)
		# [child, tab_tabel, position)
		self.noteBook.insert_page(frame, gtk.Label( _("Mouse") ) )
		
	def debug_tab(self):
		'''
		The debuging Preff Tab.
		
		Arguments:
		- self: The main object pointer.
		'''
		
		frame = gtk.Frame()
		
		debugBox = gtk.VBox(spacing = 6)
		
		levelHBox = gtk.HBox(spacing = 4)
		
		levellabel = gtk.Label( _("Debugging Level: ") )
		levellabel.set_alignment(0.0, 0.5)
		levellabel.show()
		levelHBox.pack_start(levellabel, False, False)
		
		# create an Adjustment object - [value=0, lower=0, upper=0, step_incr=0, page_incr=0, page_size=0]
		adj = gtk.Adjustment(self.cfg.getint("main", "debugLevel"), 10, 50, 10, 1, 0)
		# creates a spin button object - [adjustment, climb_rate, digits]
		levelSpin - gtk.SpinButton(adj, 0.0, 0)
		# sets the "wrap" property - True = spin button value wraps around to the opposite limit when the
		# upper of lower limit of the range is exceeded
		levelSpin.set_wrap(True)
		levelHBox.pack_start(levelSpin, False, False)
		levelSpin.connect("value-changed", self._spinChanged, "main", "debugLevel")
		
		debugBox.pack_start(levelHBox, False, False)
		
		debugBox.show_all()
		
		frame.add(debugBox)
		frame.show()
		
		self.noteBook.insert_page(frame, gtk.Label( _("Debug") ) )
		
	def show_alg_pref(self, widget, liststore):
		# ?
		dlg = dialogs.IdmSettings(self.cfg, self.selected_idm, self.selected_idm_stgs)
		dlg.set_transient_for(self)
		dlg.set_destroy_with_parent(True)
		
	def acceptButtonClick(self, *args):
		'''
		Accept button callback. This will apply to the settings and close the 
		preferences GUI.
		
		Arguments:
		- self: The main object pointer.
		- *args: The button event arguments.
		'''
		
		env.configPath = "userSettings.cfg"
		self.cfg.write(open(env.configPath, "w"))
		self.destroy()
		
	def _tree_view_click(self, widget, conf_button):
		'''
		Row Selection Event.
		
		Enables/Disables the conf_button whether the
		selected algorithm can be configured or not.
		
		Arguments:
		- widget: The gtk Widget.
		- conf_button: The configuration button object.
		'''
		
		# 
		ts = widget.get_selection()
		model, it = ts.get_selected()
		path = model.get_path(it)[0]
		if model[path][0] and model[path][3]:
			self.selected_idm = model[path][1]
			self.selected_idm_stgs = model[path][3]
			conf_button.set_sensitive(True)
			
	def _toggle_cell_changed(self, cell, path, model):
		'''
		ListStore RadioButton Value Changer.
		'''
		
		# ?
		if model[path][0]:
			return false
		
		for pth in range(len(model)):
			pth = str(pth)
			if pth == path:
				model[pth][0] = True
				self.cfg.set("main", "algorithm", model[pth][1].lower())
			else:
				model[pth][0] = False
	
	def _enable_disable_addon(self, cell, path, model):
		'''
		ListStore RadioButton Value Changer.
		'''
		
		model[path][0] = not model[path][0]
		
		cur = self.cfg.getList("main", "addon")
		
		if model[path][1] in cur:
			cur.remove(model[path][1].lower())
		else:
			cur.append(model[path][1].lower())
		
		self.cfg.setList("main", "addon", cur)
		
	def _checkToggled(self, widget, section, option):
		'''
		Sets the new value in the settings object for the toggled checkbox.
		
		Arugments:
		- self: The main object pointer.
		- widget: The checkbox
		- section: The section of the settings object.
		- option: The option in the section.
		'''
		# 
		self.cfg.set(section, option, str(widget.get_value_as_int()))
		
	def _spinChanged(self, widget, section, option):
		'''
		Sets the new value int he settings object for the toggled checkbox.
		
		Arguments:
		- self: The main object pointer.
		- widget: The checkbox.
		- section: The section of the settings object.
		- option: The option in the section.
		'''
		# 
		self.cfg.set(section, option, str(widget.get_value_as_int()))
	
	def applyButtonClick(self, *args):
		'''
		Apply button callback. This will apply the settings
		
		Arguments:
		- self: The main object pointer.
		- *args: The button event arguments.
		'''
		# 	
		env.configPath = "userSettings.cfg"
		self.cfg.write(open(env.configPath, "w"))
	
	def _comboChanged(self, widget, section, option, modes=None):
		'''
		On combo change. This function is the callback for the on_change
		event.
		
		Arguments:
		- self: The main object pointer.
		- widget: The widget pointer.
		- section: The section of the settings object.
		- option: The option in the section.
		- modes: The new value.
		'''
		# 
		model = widget.get_model()
		index = widget.get_active()
		val = (modes and modes[model[index][0]]) or model[index][0]
		self.cfg.set(section, option, val)
		
	def addSpin(self, label, var, startValue, section, option, min_=1, max_=15):
		'''
		Creates a new spin button inside a HBox and return it.
		
		Arguments:
		- self: The main object pointer.
		- label: The spin button label.
		- var: The prefference dict variable.
		- startValue: The start value.
		'''
		# 
		spinHbox = gtk.HBox(spacing=4)
		
		spinLb1 = gtk.Label(label)
		spinLb1.set_alignment(0.0, 0.5)
		spinLb1.show()
		spinHbox.pack_start(spinLb1, False, False)
		
		# 
		adj = gtk.Adjustment(startValue, min_, max_, 1, 1, 0)
		spingButton = gtk.SpinButton(adj, 0.0, 0)
		spinButton.set_wrap(True)
		spinButton.connect("value-changed", self._spinChanged, section, option)
		spinHbox.pack_start(spinButton, 0.0, 0)
		
		# 
		spin.Lb1.set_mnemonic_widget(spinButton)
		
		return spinHbox
		
	def close(self, *args):
		'''
		Closes the prefferences GUI without saving the changes.
		
		Arguments:
		- self: The main object pointer.
		- *args: The button event arguments.
		'''
		# 
		self.destroy()
		
	def showPreffGui(controller):
		'''
		Starts the preffGui.
		
		Arguments:
		- mouseTrap: The mouseTrap object pointer.
		'''
		# 
		gui = PreffGui(controller)
		gui.setWindowsIcon()
		gui.buildInterface()
