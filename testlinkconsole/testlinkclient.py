from testlink import TestlinkAPIClient

class TestlinkClient:
    def __init__(self, apiclient):
        self.apiclient = apiclient

    def listProjects(self):
        result=[]
        for projet in self.apiclient.getProjects():
            result.append(
                    {
                        'id': projet['id'],
                        'name' : projet['name'],
                        })
        return result

    def listTestPlans(self, projectid):
        result=[]
        for campagne in self.apiclient.getProjectTestPlans(testprojectid=projectid):
            result.append(
                    {
                        'id' : campagne['id'],
                        'name' : campagne['name'],
                        })
        return result
