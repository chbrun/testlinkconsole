from libs.iBDTestPlugin import IBDTestPlugin

class BDLocalPlugin(IBDTestPlugin):
    def activate(self):
        super(BDLocalPlugin, self).activate()
        return "BDLocal plugin actif"

    def deactivate(self):
        super(BDLocalPlugin, self).deactivate()
        return "BDLocal plugin inactif"

    def run(self, browser, script):
        print "BDLocal run %s with %s" % (script, browser)
