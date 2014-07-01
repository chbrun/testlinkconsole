#import unittest2 as unittest
import unittest
import mox

from testlinkclient import TestlinkClient
from testlink import TestlinkAPIClient

class TestingClassTestlinkAPIClient(TestlinkAPIClient):
    def __init__(self, server_url,  devkey):
        super(TestingClassTestlinkAPIClient, self).__init__(server_url, devkey)

class TestlinkClientTest(unittest.TestCase):

    def setUp(self):
        self.mocker = mox.Mox()
        self.apiclient = self.mocker.CreateMock(TestingClassTestlinkAPIClient)
        self.testlinkclient = TestlinkClient(self.apiclient)

    def testListProjects(self):
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
        self.assertEquals(self.testlinkclient.listProjects(),projectsOut)

    def testListTestPlans(self):
        testPlansIn=[
                {'id':'1', 'name':'campagne1', 'description':'description1'}, 
                ]
        testPlansOut=[
                {'id':'1', 'name':'campagne1'}, 
                ]
        self.apiclient.getProjectTestPlans(testprojectid=1).AndReturn(testPlansIn)
        self.mocker.ReplayAll()
        self.assertEquals(self.testlinkclient.listTestPlans(1), testPlansOut)

    @unittest.skip("TODO")
    def testListTestCasess(self):
        raise Exception('TODO')

    @unittest.skip("TODO")
    def testRunTestPlan(self):
        raise Exception('TODO')

    @unittest.skip("TODO")
    def testRunTest(self):
        raise Exception('TODO')

if __name__ == '__main__':
    unittest.main()
