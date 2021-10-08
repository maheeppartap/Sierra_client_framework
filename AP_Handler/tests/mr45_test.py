import os
import unittest
from AP_Handler.derived_AP.ciscoMR45 import MR45


class MyTestCase(unittest.TestCase):
    def test_get_info(self):
        # m = MR45()
        x = MR45.get_list_of_devices(network='SVT-MR45')

    def test_set_config(self):
        pass


if __name__ == '__main__':
    unittest.main()
