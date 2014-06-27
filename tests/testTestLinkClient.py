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

    def testListProjets(self):
        projetsIn=[
                {'id':'1', 'name':'projet1', 'description':'description1'}, 
                {'id':'2', 'name':'projet2', 'description':'description2'},
                ]
        projetsOut=[
                {'id':'1', 'name':'projet1'}, 
                {'id':'2', 'name':'projet2'},
                ]
        self.apiclient.getProjects().AndReturn(projetsIn)
        self.mocker.ReplayAll()
        self.assertEquals(self.testlinkclient.listProjets(),projetsOut)

    def testListCampagnes(self):
        campagnesIn=[
                {'id':'1', 'name':'campagne1', 'description':'description1'}, 
                ]
        campagnesOut=[
                {'id':'1', 'name':'campagne1'}, 
                ]
        self.apiclient.getProjectTestPlans(testprojectid=1).AndReturn(campagnesIn)
        self.mocker.ReplayAll()
        self.assertEquals(self.testlinkclient.listCampagnes(1), campagnesOut)

    @unittest.skip("TODO")
    def testListTests(self):
        raise Exception('TODO')

    @unittest.skip("TODO")
    def testRunCampagne(self):
        raise Exception('TODO')

    @unittest.skip("TODO")
    def testRunTest(self):
        raise Exception('TODO')

if __name__ == '__main__':
    unittest.main()
