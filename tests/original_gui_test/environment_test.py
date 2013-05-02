# MouseTrap GUI Test
# from: /app/environment.py.in
# Holds mouseTrap internal information
# environment.py

# This module provides a number of functions
# and variables that can be used to manipulate different parts of the Python runtime environment.
import sys
import os # Misc. Operating System Interfaces
import gtk # GIMPToolkit

__id__        = "$Id$"
__version__   = "$Revision$"
__date__      = "$Date$"
__copyright__ = "Copyright (c) 2008 Flavio Percoco Premoli."
__license__   = "GPLv2"

import sys
import os
import gtk

## MouseTrap's PID
pid = os.getpid()

## mouseTrap Version
version     = "@MOUSETRAP_VERSION@"

## "--prefix" parameter used when configuring the build.
prefix      = "@prefix@"

## The package name (should be "mousetrap").
package     = "@PACKAGE@"

## The name of the data directory (usually "share").
datadirname = "%s/@DATADIRNAME@" % prefix

## Directly mouseTrap data dir
mTDataDir = "%s/mouseTrap" % datadirname

## The username
# username = os.getlogin()

## The current running desktop manager.
try:
    dbusd.bus.get_object("org.gnome.SessionManager", "/")
    desktop = "gnome"
except:
    desktop = "other"

## The name of the O.S
osName = os.name

## The application's path
appPath = os.path.dirname(__file__)

## The user's home directory
home = os.path.expanduser("~")

## Configurations dir
configPath = home + "/.mousetrap/"

## Configurations dir
configPath = "%s/.mousetrap/" % home

## Scripts Path
scriptsPath = "%s/scripts/" % configPath

## Profiles Path
profilesPath = "%s/profiles/" % scriptsPath

## The config file
configFile = configPath + "userSettings.cfg"

## The debug file
debugFile = configPath + "mouseTrap.debug"

## The language path
langPath = "%s/locale/" % datadirname

## Screen Resolution
screen       = { 'width'  : gtk.gdk.screen_width(),
                 'height' : gtk.gdk.screen_height()}

## Mose Movement Modes
mouseModes = { }

###################################################
#                                                 #
#          MOUSETRAP'S STATES DEFINITION          #
#                                                 #
###################################################

## Mousetrap is active and the mouse pointer can be moved
ACTIVE = "active"

## Mousetrap is active and the click dialog is not hidden.
CLKDLG = "clk-dialog"