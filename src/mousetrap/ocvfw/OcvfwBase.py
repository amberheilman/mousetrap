# -*- coding: utf-8 -*-

# Ocvfw
#
# Copyright 2009 Flavio Percoco Premoli
#
# This file is part of Ocvfw.
#
# Ocvfw is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License v2 as published
# by the Free Software Foundation.
#
# Ocvfw is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ocvfw.  If not, see <http://www.gnu.org/licenses/>>.

"""Little  Framework for OpenCV Library."""

__id__        = "$Id$"
__version__   = "$Revision$"
__date__      = "$Date$"
__copyright__ = "Copyright (c) 2008 Flavio Percoco Premoli"
__license__   = "GPLv2"

import os
import re
import time
from .. import debug
from .. import commons as co


class OcvfwBase:
    
    def __init__( self, capture ):
        """
        Initialize the module and set its main variables.
        """

        self.img          = None
        self.mhi          = None
        self.img_lkpoints = { "current" : [],
                              "last"    : [],
                              "points"  : [] }

        self.__lk_swap = False
        self.imageScale   = 1.5

    def set(self, key, value):
        """
        Changes some class settings

        Arguments:
        - self: The main object pointer.
        - key: The key to change.
        - value: The new value.
        """
        if hasattr(self, "%s" % key):
            getattr(self, "%s" % key)(value)
            debug.debug("OcvfwBase", "Changed %s value to %s" % (key, value))
            return True
        
        debug.debug("OcvfwBase", "%s not found" % (key))
        return False

    def lk_swap(self, set=None):
        """
        Enables/Disable the lk points swapping action.

        Arguments:
        - self: The main object pointer.
        - set: The new value. If None returns the current state.
        """
        
        if set is None:
            return self.__lk_swap
        
        self.__lk_swap = set

    def set_lkpoint(self, point):
        """
        Set a point to follow it using the Lucas Kanade method.

        Arguments:
        - self: The main object pointer.
        - point: A co.cv.cvPoint Point.
        """

        point = ( point.x, point.y )

        self.img_lkpoints["current"] = [ co.cv.cvPointTo32f ( cvPoint ) ]

        if self.img_lkpoints["current"]:
            co.cv.cvFindCornerSubPix (
                self.grey,
                self.img_lkpoints["current"],
                co.cv.cvSize (20, 20), co.cv.cvSize (-1, -1),
                co.cv.cvTermCriteria (co.cv.CV_TERMCRIT_ITER | co.cv.CV_TERMCRIT_EPS, 20, 0.03))

            point.set_opencv( cvPoint )
            self.img_lkpoints["points"].append(point)

            setattr(point.parent, point.label, point)

            if len(self.img_lkpoints["last"]) > 0:
                self.img_lkpoints["last"].append( self.img_lkpoints["current"][0] )

            debug.debug( "ocvfw", "cmSetLKPoints: New LK Point Added" )
        else:
            self.img_lkpoints["current"] = []

    def clean_lkpoints(self):
        """
        Cleans all the registered points.

        Arguments:
        - self: The main object pointer
        """

        self.img_lkpoints = { "current" : [],
                              "last"    : [],
                              "points"  : [] }

    def show_lkpoints(self):
        """
        Callculate the optical flow of the set points and draw them in the image.

        Arguments:
        - self: The main object pointer.
        """

        # calculate the optical flow
        optical_flow = co.cv.cvCalcOpticalFlowPyrLK (
            self.prevGrey, self.grey, self.prevPyramid, self.pyramid,
            self.img_lkpoints["last"], len( self.img_lkpoints["last"] ),
            co.cv.cvSize (20, 20), 3, len( self.img_lkpoints["last"] ), None,
            co.cv.cvTermCriteria (co.cv.CV_TERMCRIT_ITER|co.cv.CV_TERMCRIT_EPS, 20, 0.03), 0)

        if isinstance(optical_flow[0], tuple):
            self.img_lkpoints["current"], status = optical_flow[0]
        else:
            self.img_lkpoints["current"], status = optical_flow


        # initializations
        counter = 0
        new_points = []

        for point in self.img_lkpoints["current"]:

            if not status[counter]:
                continue

            # this point is a correct point
            current = self.img_lkpoints["points"][counter]
            current.set_opencv(co.cv.cvPoint(int(point.x), int(point.y)))

            new_points.append( point )

            setattr(current.parent, current.label, current)

            # draw the current point
            current.parent.draw_point(point.x, point.y)

            # increment the counter
            counter += 1


        #debug.debug( "ocvfw", "cmShowLKPoints: Showing %d LK Points" % counter )

        # set back the self.imgPoints we keep
        self.img_lkpoints["current"] = new_points


    def swap_lkpoints(self):
        """
        Swap the LK method variables so the new points will be the last points.
        This function has to be called after showing the new points.

        Arguments:
        - self: The main object pointer.
        """

        # swapping
        self.prevGrey, self.grey               = self.grey, self.prevGrey
        self.prevPyramid, self.pyramid         = self.pyramid, self.prevPyramid
        self.img_lkpoints["last"], self.img_lkpoints["current"] = \
                                   self.img_lkpoints["current"], self.img_lkpoints["last"]

