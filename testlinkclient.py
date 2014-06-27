from testlink import TestlinkAPIClient

class TestlinkClient:
    def __init__(self, apiclient):
        self.apiclient = apiclient

    def listProjets(self):
        result=[]
        for projet in self.apiclient.getProjects():
            result.append(
                    {
                        'id': projet['id'],
                        'name' : projet['name'],
                        })
        return result
