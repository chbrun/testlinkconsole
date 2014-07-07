from yapsy.IPlugin import IPlugin

class IBDTestPlugin(IPlugin):

    def activate(self):
        super(IBDTestPlugin, self).activate()
        return "IBDTestPlugin actif"

    def deactivate(self):
        super(IBDTestPlugin, self).deactivate()
        return "IBDTestPlugin inactif"
