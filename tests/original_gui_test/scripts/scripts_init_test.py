# MouseTrap GUI Test
# from: /app/ui/scripts/__init__.py
# ui.scripts.__init__test.py

import re # Regular Expression Operations
import os # Misc. Operating System Interfaces

def get_scripts_list():
	'''
	Checks the addons folder and gets the
	list of present (preset?) addons.
	
	Arguments:
	- self: The main object pointer.
	'''
	
	# 
	reg = re.compile(r'([A-Za-z0-9]+)\.py$', re.DOTALL)
	dirname = os.path.dirname(__file__)
	return [ mod[0] for mod in [ reg.findall(f) for f in os.listdir("%s/" % dirname) if "__init__" not in f] if mod ]
	
def get_script_class(script_name):
	# 
	script = __import__(script_name, globals(), locals())
	return getattr(script, "ScriptClass")
