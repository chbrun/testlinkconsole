import unittest
import mox

from plugins.behat import BehatPlugin

class TestBehatPlugin(unittest.TestCase):

    def setUp(self):
        self.plugin = BehatPlugin()

    def testactivate(self):
        self.assertEquals(self.plugin.activate(), "Behat plugin actif")

    def testdeactivate(self):
        self.assertEquals(self.plugin.deactivate(), "Behat plugin inactif")

    def test_getFileResult(self):
        self.assertEquals(self.plugin.getFileResult('script_a_lancer.feature'),'script_a_lancer')

    @unittest.skip("TODO")
    def testrun(self):
        raise Exception("TODO")

    @unittest.skip("TODO")
    def testresult(self):
        raise Exception("TODO")

if __name__ == '__main__':
    unittest.main()
