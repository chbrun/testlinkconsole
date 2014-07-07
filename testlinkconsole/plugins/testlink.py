from libs.iBDTestPlugin import IBDTestPlugin

class TestlinkPlugin(IBDTestPlugin):
    def activate(self):
        super(TestlinkPlugin, self).activate()
        return "Testlink plugin actif"

    def deactivate(self):
        super(TestlinkPlugin, self).deactivate()
        return "Testlink plugin inactif"

    def run(self, browser, script):
        print "Testlink run %s with %s" % (script, browser)
