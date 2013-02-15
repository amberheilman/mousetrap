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

import time
import debug
import commons as co
import cv2
import cv2.cv as cv #remove
import numpy

class OcvfwBase:
    
    def __init__( self ):
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

    def new_image(self, size, num, ch):
        """
        Creates a new image 
        """

        #if type(size) == "<type 'tuple'>":
            #size = co.cv.cvSize( size[0], size[1])
        return co.cv.CreateImage( (size[0], size[1]), num, ch)# was size'

    def set_camera_idx(self, idx):
        """
        Changes the camera device index.

        Arguments:
        - self: The main object pointer.
        - idx: The camera index. For Example: 0 for /dev/video0
        """
        self.idx = idx

    def wait_key(self, num):
        """
        Simple call to the co.cv.WaitKey function, which has to be called periodically.

        Arguments:
        - self: The main object pointer.
        - num: An int value.
        """
        return co.cv.WaitKey(num)
    
    def start_camera(self, params = None):
        """
        Starts the camera capture using co.hg.

        Arguments:
        - params: A list with the capture properties. NOTE: Not implemented yet.
        """
        self.capture = cv.CaptureFromCAM(int(self.idx) )
        debug.debug( "ocvfw", "cmStartCamera: Camera Started" )
    
    def query_image(self, bgr=False, flip=False):
        """
        Queries the new frame.

        Arguments:
        - self: The main object pointer.
        - bgr: If True. The image will be converted from RGB to BGR.

        Returns The image even if it was stored in self.img
        """

        frame = self.capture.QueryImage()
        if not  self.img:
            self.storage        = cv.CreateMemStorage(0)
            self.imgSize        = [int(frame_width), int(frame_height)]
	    self.img            = cv.CreateImage ( self.imgSize, 8, 3 )
            #self.img.origin     = frame.origin
            self.grey           = cv.CreateImage ( self.imgSize, 8, 1 )
            self.yCrCb          = cv.CreateImage ( self.imgSize, 8, 3 )
            self.prevGrey       = cv.CreateImage ( self.imgSize, 8, 1 )
            self.pyramid        = cv.CreateImage ( self.imgSize, 8, 1 )
            self.prevPyramid    = cv.CreateImage ( self.imgSize, 8, 1 )
            self.small_img      = cv.CreateImage( 
				  ((self.img.width/self.imageScale),
				  (self.img.height/self.imageScale)), 8, 3 )
<<<<<<< Updated upstream
=======
	debug.debug("Ocvfw", self.img) #remove
>>>>>>> Stashed changes

        self.img = frame
	#fix me cv2.cvtColor(self.img, cv.CV_BGR2GRAY)

        self.wait_key(10)
        return True
    
    def set_lkpoint(self, point):
        """
        """
        Calculate the optical flow of the set points and draw them in the image.

        Arguments:
        - self: The main object pointer.
        """

	debug.debug("Ocvfw", type(self.img_lkpoints["last"])) #remove
        nextPts, status, err = cv.CalcOpticalFlowPyrLK (
	     self.prevGrey, 
             self.grey, 
             self.prevPyramid, 
             self.pyramid,
             [],
             (5,5),
             3,#pyr number
             (cv.CV_TERMCRIT_ITER | cv.CV_TERMCRIT_EPS, 10, 0.01),
             0)


<<<<<<< Updated upstream
=======
        Arguments:
        - self: The main object pointer.
        """

	debug.debug("Ocvfw", type(self.img_lkpoints["last"])) #remove
        nextPts, status, err = cv.CalcOpticalFlowPyrLK (
	     self.prevGrey, 
             self.grey, 
             self.prevPyramid, 
             self.pyramid,
             [],
             (5,5),
             3,#pyr number
             (cv.CV_TERMCRIT_ITER | cv.CV_TERMCRIT_EPS, 10, 0.01),
             0)


	debug.debug("Ocvfw", nextPts) #remove
	debug.debug("Ocvfw", status) #remove
	debug.debug("Ocvfw", err) #remove

>>>>>>> Stashed changes
        if isinstance(nextPts, tuple):
            self.img_lkpoints["current"], status = nextPts, status
        else:
            self.img_lkpoints["current"], status = nextPts


        # initializations
        counter = 0
        new_points = []

    

    def __init__(self):
        """
        Initialize the module and set its main variables.
        """
        co.cv = __import__("ctypesopencv.cv",
                        globals(),
                        locals(),
                        [''])
        
        co.hg = __import__("ctypesopencv.cv",
                        globals(),
                        locals(),
                        [''])
 
        OcvfwBase.__init__(self)


class OcvfwPython(OcvfwBase):
    """
        - haarCascade: The selected cascade.
        - methode: The search method to use. DEFAULT: co.cv.CV_HAAR_DO_CANNY_PRUNING.

        Returns a list with the matches.
        """

        cascade = cv.Load( haarCascade) #, self.imgSize )

        if not cascade:
            debug.exception( "ocvfw", "The Haar Classifier Cascade load failed" )
	cv2.resize( self.img, self.small_img, cv.CV_INTER_LINEAR )

        #co.cv.ClearMemStorage( self.storage )

        points = cv.HaarDetectObjects( self.small_img, cascade, self.storage, 1.2, 2, method, (20, 20) )
        if points:
	    matches = [ [ ( int(r[0][0]*self.imageScale), int(r[0][1]*self.imageScale)), \
                          ( int((r[0][0]+r[0][3])*self.imageScale), int((r[0][0]+r[0][2])*self.imageScale) )] \
                          for r in points]
			
            debug.debug( "ocvfw", "cmGetHaarPoints: detected some matches" )
            return matches

    def get_haar_roi_points(self, haarCascade, rect, origSize=(0, 0), method=co.cv.CV_HAAR_DO_CANNY_PRUNING):
        """
        Search for points matching the haarcascade selected.

        Arguments:
        - self: The main object pointer.
        - haarCascade: The selected cascade.
        - methode: The search method to use. DEFAULT: co.cv.CV_HAAR_DO_CANNY_PRUNING.

        Returns a list with the matches.
        """

        cascade = co.cv.Load( haarCascade ) #, self.imgSize )
        if not cascade:
            debug.exception( "ocvfw", "The Haar Classifier Cascade load failed" )

        #remove, DNE co.cv.ClearMemStorage(self.storage)
<<<<<<< Updated upstream
=======
	debug.debug("Ocvfw", rect) #remove
>>>>>>> Stashed changes
 	#imageROI = cv.GetSubRect(self.img, rect)

        if cascade:
            points = cv.HaarDetectObjects( self.img, cascade, self.storage,
                                    1.2, 2, method, (20,20) ) #replace imageROI with self.img
        else:
            debug.exception( "ocvfw", "The Haar Classifier Cascade load Failed (ROI)" )

        if points:
            matches = [ [ ( int(r[0][0]+origSize[0]), int(r[0][1]+origSize[1])), \
                          ( int(r[0][0]+r[0][3]+origSize[0]), int(r[0][1]+r[0][2]+origSize[1] ))] \
                          for r in points] #replaced x with [0][0] and y with [0][1] and height with [0][2] and width with [0][3]
            debug.debug( "ocvfw", "cmGetHaarROIPoints: detected some matches" )
            return matches




                self.buf[i] = co.cv.CreateImage( imgSize, 8, 1 )
                co.cv.cvZero( self.buf[i] )

        idx1 = self.lastFm

        # convert frame to grayscale
        cv.cvtColor( img, self.buf[self.lastFm], cv.CV_BGR2GRAY )

        # index of (self.lastFm - (n_-1))th frame
        idx2 = ( self.lastFm + 1 ) % n_
        self.lastFm = idx2

        silh = self.buf[idx2]
