# from nose.tools import assert_list_equal

__author__ = 'Hao Lin'

import unittest
import utils.ftp_handlers.ftp_handler as ftp_handler

class TestFtp(unittest.TestCase):

    def setUp(self):
        pass

    def test_numbers(self):
        self.assertEqual(3, int('3'))

    def test_connection(self):
        handler = ftp_handler.FtpHandlerFactory.create_handler("WMG")
        new_xml_list = handler.get_new_xml_list()
        update_xml_list = handler.get_update_xml_list()
        self.assertListEqual(new_xml_list, update_xml_list)


if __name__ == '__main__':
    unittest.main()