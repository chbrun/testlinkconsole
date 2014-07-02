import unittest
import mox

from plugins.behave import BehavePlugin

class TestBehavePlugin(unittest.TestCase):

    def setUp(self):
        self.plugin = BehavePlugin()

    def testactivate(self):
        self.assertEquals(self.plugin.activate(), "Behave plugin actif")

    def testdeactivate(self):
        self.assertEquals(self.plugin.deactivate(), "Behave plugin inactif")

    @unittest.skip("TODO")
    def testrun(self):
        raise Exception("TODO")


if __name__ == '__main__':
    unittest.main()
