#import unittest2 as unittest
import unittest
import mox
import ConfigParser

from libs.consoleBase import ConsoleBase

class TestconsoleBase(unittest.TestCase):

    def setUp(self):
        self.consoleBase = ConsoleBase(ConfigParser.RawConfigParser())

    def test_help_config(self):
        self.assertEquals(self.consoleBase.help_config(),None)
    
    @unittest.skip('todo')
    def test_help_save(self):
        self.assertEquals(self.consoleBase.help_save(),None)
        
    def test_help_get(self):
        self.assertEquals(self.consoleBase.help_get(),None)
    
    def test_help_set(self):
        self.assertEquals(self.consoleBase.help_set(),None)

if __name__ == '__main__':
    unittest.main()
