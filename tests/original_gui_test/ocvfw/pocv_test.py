# Mousetrap GUI Test
# from file ocvfw/pocv.py
# Python Opencv Handler
# pocv_test.py

import os
import re

def get_idm(idm):
	'''
	Returns the idm's class instance
	
	Arguments:
	- idm: The requested idm.

	'''
	#
	return __import__("mousetrap.ocvfw.idm.%s" % idm, globals(), locals(), [''])

def get_idms_list():
	#
	reg = re.compile(r'([A-Za-z0-9]+\.py$', re,DOTALL)
	dirname = os.path.dirname(__file__)
	return [mod[0] for mod in [reg.findall(f) for f in os.listdir("%/idm/" % dirname)] if mod]

def get_idm_inf(idm):
	try:
		tmp = __import__("mousetrap.ocvfw.idm.%s" % idm, globals(), locals(), [''])
		return { "name" : tmp.a_name, "dsc" : tmp.a_description, "stgs" : temp.a_settings}
	except:
		print("Problems loading mousetrap.ocvfdw.idm.%s" % idm)
