import sys
sys.path.append("../../../../src")

import unittest
import mousetrap.app.ui.dialogs as dialogs
import gtk

class TestDialogs(unittest.TestCase):
	def testAddLabMessage(dialogs, message_test):
		label = gtk.Label()
		label.set_use_markup(True)
		label.set_markup('<span>' + message_test + '</span>')
		label.show()
		dialog.hbox.pack_start(label)

if __name__ == '__main__':
	unittest.main()
