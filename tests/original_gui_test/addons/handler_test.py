# MouseTrap GUI Test
# from: /app/addons/handler.py
# addons.handler_test.py
# for the AddonsBase class

import os, re

class AddonsHandler(object):
	#
	def __init__(self, controller):
		'''
		This is the AddonsHandler init function
		
		Arguments:
		- self: The main object pointer.
		- controller: The mousetrap's controller.
		'''
		# sets self.ctr to be the mousetrap controller
		self.ctr = controller
		
	def get_addons_list(self):
		'''
		Checks the addons folder and gets the
		list of present (preset?) addons
		
		Arguments:
		- self: The main object pointer.
		'''
		# 
		reg = re.compile(r'([A-Za-z0-9]+)\.py$', re.DOTALL)
		dirname = os.path.dirname(__file__)
		return [mod[0] for mod in [reg.findall(f) for f in os.listdir("%s/" % dirname) if "handler" not in f] if mod ]
		
	def get_addon_inf(self, addon):
		'''
		Gets basic information (Name, Description, Settins)
		
		Arguments:
		- self: The main object pointer.
		- addon: The addon to explore.
		'''
		# 
		try:
			tmp = __import__("mousetrao.add.addons.%s" % addon,
							globals(),
							locals(),
							[''])
			
			return { "name" : tmp.a_name, "dsc" : tmp.a_description, "stgs" : tmp.a_settings}
		except:
			print("Problems loading mousetrap.app.addons.%s" % addon)

class AddonsBase(object):
	#
	def __init__(self, controller):
		'''
		This is the AddonsBase init function
		
		Arguments:
		- self: The main object pointer.
		- controller: The mousetrap's controller.
		'''
		
		self.ctr = controller
		self.cfg = controller.cfg
		self.itf = self.ctr.itf
		
	def statusbar_message(self, msg):
		'''
		Writes a message in the stausbar
		
		Arguments:
		- self: The main object pointer.
		- msg: The message.
		'''
		# 
		self.itf.statusbar.push(self.itf.statusbar_id, msg)
		
	def add_item(self, item):
		'''
		Adds on gtk widget to the addons vbox.
		
		Arguments:
		- self: The main object pointer.
		- item: The item to add.
		'''
		# 
		self.itf.adds_vbox.pack_start(item, True, True)