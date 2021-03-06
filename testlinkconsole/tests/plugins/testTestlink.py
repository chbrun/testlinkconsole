import unittest
import mock
import mox
import ConfigParser

from plugins.ptestlink import TestlinkPlugin
from testlink import TestlinkAPIClient

class TestingClassTestlinkAPIClient(TestlinkAPIClient):
    def __init__(self, server_url,  devkey):
        super(TestingClassTestlinkAPIClient, self).__init__(server_url, devkey)


class TestTestlinkPlugin(unittest.TestCase):

    def setUp(self):
        self.mocker = mox.Mox()
        self.apiclient = self.mocker.CreateMock(TestingClassTestlinkAPIClient)
        self.plugin = TestlinkPlugin()
        try:
            self.plugin.init(ConfigParser.RawConfigParser())
        except IOError:
            self.plugin.testlinkclient = self.apiclient

    def test_activate(self):
        self.assertEquals(self.plugin.activate(), "Testlink plugin actif")

    def test_deactivate(self):
        self.assertEquals(self.plugin.deactivate(), "Testlink plugin inactif")

    @unittest.skip('TODO')
    @mock.patch('__builtin__.print')
    def test_run(self, mock_print):
        mock_print.assert_has_calls([])
        self.assertEquals(self.plugin.run('profile','script'),None)

    def test_list_projects(self):
        projectsIn=[
                {'id':'1', 'name':'projet1', 'description':'description1'},
                {'id':'2', 'name':'projet2', 'description':'description2'},
                ]
        projectsOut=[
                {'id':'1', 'name':'projet1'},
                {'id':'2', 'name':'projet2'},
                ]
        self.apiclient.getProjects().AndReturn(projectsIn)
        self.mocker.ReplayAll()
        self.assertEquals(self.plugin.list_projects(),projectsOut)

    def test_list_testplans(self):
        testPlansIn=[
                {'id':'1', 'name':'campagne1', 'description':'description1'},
                    ]
        testPlansOut=[
                {'id':'1', 'name':'campagne1'},
                    ]
        self.apiclient.getProjectTestPlans(testprojectid=1).AndReturn(testPlansIn)
        self.mocker.ReplayAll()
        self.assertEquals(self.plugin.list_testplans(1), testPlansOut)

    def test_list_testcases(self):
        testCasesIn={'test1' : [
            {'tcase_id':'1', 'tcase_name':'test1', 'description':'description du test 1', 'full_external_id':'234'},
                ]}
        testCasesOut=[
                {'id':'1', 'name':'test1', 'extid': '234'},
                ]
        self.apiclient.getTestCasesForTestPlan(testplanid=1, execution_type=2).AndReturn(testCasesIn)
        self.mocker.ReplayAll()
        self.assertEquals(self.plugin.list_testcases(1), testCasesOut)

    @unittest.skip('TODO')
    def test_get_info_project(self):
        pass

    @unittest.skip('TODO')
    def test_get_info_testplan(self):
        pass

    @unittest.skip('TODO')
    def test_get_info_testcase(self):
        pass

    @unittest.skip('TODO')
    def test_run_testplan(self):
        pass

    @unittest.skip('TODO')
    def test_run_testcase(self):
        pass

if __name__ == '__main__':
    unittest.main()
