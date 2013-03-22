"""
Camera Backend
"""

try:
    import gtk
except ImportError:
    debug.info("Camera", "Gtk not imported")

import cv2 as cv
import debug
from gi.repository import GObject

def singleton(self, instance={}):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
            debug.debug("camera_backend", "New Singleton Add (%s)" % cls)
        return instances[cls]
    return getinstance


@singleton
class Camera(object):


    def __init__(self):
	singleton(self)
	self.idx = idx
	self.capture = capture

    def set_camera_idx(self, idx):
        """
        Changes the camera device index.

        Arguments:
        - self: The main object pointer.
        - idx: The camera index. For Example: 0 for /dev/video0
        """
        self.idx = idx

    def start_camera(self, params = None):
        """
        Starts the camera capture.

        Arguments:
        - params: A list with the capture properties.
        """
        self.capture = cv.VideoCapture( int(self.idx) )
        debug.debug( "camera_backend", "Camera Status: Camera Started" )

	return self.capture

    wait_key(self, num):
        """
        Simple call to the WaitKey function, which has to be called periodically.

        Arguments:
        - self: The main object pointer.
        - num: An int value.
        """
        return cv2.WaitKey(num)

    def set_async(self, fps=100, async=False):
        """
        Sets/Unsets the asynchronous property.

        Arguments:
        - self: The main object pointer
        - fps: The frames per second to be queried.
        - async: Enable/Disable asynchronous image querying. Default: False
        """

        self.fps   = fps
        self.async = async

        if self.async:
            GObject.timeout_add(self.fps, self.sync)
