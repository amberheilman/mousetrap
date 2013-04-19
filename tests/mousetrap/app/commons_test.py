import sys
sys.path.append("../../../src")

import unittest
import mousetrap.app.commons as commons

class TestCommons(unittest.TestCase):
  def test_get_py_list(self):
    '''Normal Case
    '''
    dlist = [ 'test_commons_data/src/', 'test_commons_data/dira' ]
    expected = [ 'a', 'b', 'c' ]
    elist = commons.get_py_list(dlist)
    self.assertEqual(elist, expected)

if __name__ == '__main__':
  unittest.main()
