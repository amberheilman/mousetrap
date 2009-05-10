# -*- coding: utf-8 -*-

# mouseTrap
#
# Copyright 2009 Flavio Percoco Premoli
#
# This file is part of mouseTrap.
#
# mouseTrap is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# mouseTrap is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with mouseTrap.  If not, see <http://www.gnu.org/licenses/>.


"""MouseTrap's main script."""

__id__        = "$Id: mousetrap.py 30 2009-04-03 16:00:06Z flaper $"
__version__   = "$Revision: 30 $"
__date__      = "$Date: 2009-04-03 18:00:06 +0200 (vie 03 de abr de 2009) $"
__copyright__ = "Copyright (c) 2008 Flavio Percoco Premoli"
__license__   = "GPLv2"


import gtk
import gobject
from ocvfw import pocv
from ui.main import MainGui
from ui.scripts.screen import ScriptClass
from lib import mouse, httpd, dbusd, settings

class Controller():

    def __init__(self):
        """
        The MouseTrap controller init class

        Arguments:
        - self: The main object pointer.
        """

        # We don't want to load the settings each time we need them. do we?
        self.cfg = None

        self.loop = gobject.MainLoop()
        self.httpd = httpd.HttpdServer(20433)
        self.dbusd = dbusd.DbusServer()


    def start(self):
        """
        Starts the modules, views classes.

        Arguments:
        - self: The main object pointer.
        """

        if self.cfg is None:
            self.cfg = settings.load()

        if not self.dbusd.start():
            self.httpd.start()

        if self.cfg.getboolean("main", "startCam"):
            # Lets start the module
            idm = pocv.get_idm(self.cfg.get("main", "algorithm"))
            self.idm = idm.Module(self)
            self.idm.set_capture(self.cfg.getint("cam", "inputDevIndex"))

            gobject.timeout_add(150, self.update_frame)
            gobject.timeout_add(50, self.update_pointers)

        # Lets build the interface
        self.itf = MainGui(self)
        self.itf.build_interface()

        gobject.threads_init()
        self.loop.run()

    def script(self):
        """
        Returns the main script class object.

        Arguments:
        - self: The main object pointer.
        """
        return ScriptClass()

    def update_frame(self):
        self.itf.update_frame(self.idm.get_image(), self.idm.get_pointer())
        return True

    def update_pointers(self):
        self.itf.script.update_items(self.idm.get_pointer())
        return True