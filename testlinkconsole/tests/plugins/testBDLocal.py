import unittest
import mock

from plugins.bdlocal import BDLocalPlugin

class TestBDLocalPlugin(unittest.TestCase):

    def setUp(self):
        self.plugin = BDLocalPlugin()

    def test_activate(self):
        self.assertEquals(self.plugin.activate(), "BDLocal plugin actif")

    def test_deactivate(self):
        self.assertEquals(self.plugin.deactivate(), "BDLocal plugin inactif")

    @mock.patch('__builtin__.print')
    def test_run(self, mock_print):
        mock_print.assert_has_calls([])
        self.assertEquals(self.plugin.run('profile','script'),None)


if __name__ == '__main__':
    unittest.main()
