#import unittest2 as unittest
import unittest
import mox

from testlinkclient import TestlinkClient
from testlink import TestlinkAPIClient

class TestlinkClientTest(unittest.TestCase):

    #def __init__(self, *args, **kw):
    #    unittest.TestCase.__init__(self, *args, **kw)

    def setUp(self):
        self.mocker = mox.Mox()
        self.apiclient = self.mocker.CreateMock(TestlinkAPIClient)
        self.testlinkclient = TestlinkClient(self.apiclient('localhost','test'))

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

    @unittest.skip("TODO")
    def testListCampagnes(self):
        raise Exception('TODO')

    @unittest.skip("TODO")
    def testListTests(self):
        raise Exception('TODO')

    @unittest.skip("TODO")
    def testRunCampagne(self):
        raise Exception('TODO')

    @unittest.skip("TODO")
    def testRunTest(self):
        raise Exception('TODO')

