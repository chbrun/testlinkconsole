#import unittest2 as unittest
import unittest
import mock
from mock import call
import ConfigParser

from libs.consoleBase import ConsoleBase

class TestconsoleBase(unittest.TestCase):

    def setUp(self):
        self.consoleBase = ConsoleBase(ConfigParser.RawConfigParser())

    # CONFIG
    @mock.patch('__builtin__.print')
    def test_help_config(self, mock_print):
        mock_print.assert_has_calls([])
        self.assertEquals(self.consoleBase.help_config(),None)
   
    @mock.patch('__builtin__.print')
    def test_do_config(self,mock_print):
        mock_print.assert_has_calls([])
        self.assertEquals(self.consoleBase.do_config('line'),None)
   
    # SAVE
    def test_do_save(self):
        self.assertEquals(self.consoleBase.do_save('line'),None)

    @unittest.skip('todo')
    @mock.patch('__builtin__.print')
    def test_help_save(self, mock_print):
        mock_print.assert_has_calls([])
        self.assertEquals(self.consoleBase.help_save(),None)

    # GET    
    @mock.patch('__builtin__.print')
    def test_help_get(self,mock_print):
        mock_print.assert_has_calls([])
        self.assertEquals(self.consoleBase.help_get(),None)
    
    @mock.patch('__builtin__.print')
    def test_do_get(self, mock_print):
        mock_print.assert_has_calls([])
        self.assertEquals(self.consoleBase.do_get('line'),None)

    # SET
    @mock.patch('__builtin__.print')
    def test_help_set(self, mock_print):
        mock_print.assert_has_calls([])
        self.assertEquals(self.consoleBase.help_set(),None)

    @mock.patch('__builtin__.print')
    def test_do_set(self, mock_print):
        mock_print.assert_has_calls([])
        self.assertEquals(self.consoleBase.do_set('variable value'),None)

if __name__ == '__main__':
    unittest.main()
