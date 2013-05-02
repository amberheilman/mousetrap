# MouseTrap GUI Test
# from: /app/ui/i18n.py.in
# ui.i18n_test.py

"""
Provides i18n support for mouseTrap using the gettext module.  Tells
gettext where to find localized strings and creates an alias, _, that
maps to the gettext.gettext function.  This function will accept a
string and return a localized string for that string.
"""

import os # to get localdir path
import gettext # to get gettext (i18n) support

# set "gettext.gettext" to alias "_" 
# and "gettext.ngettext" to "ngettext"
_ = gettext.gettext
ngettext = gettext.ngettext

# tell gettext where to find localized strings
localedir = os.path.join("@prefix@", "@DATADIRNAME@", "locale")
gettext.bindtextdomain ("@GETTEXT_PACKAGE@", localedir)
gettext.textdomain("mousetrap")