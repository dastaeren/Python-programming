class PAM:
    _name = None
    def __init__(self,name):
        self.name = name
    def _displayName(self):
        print(self.name)

class PAM_dc(PAM):
    def _init_(_self, name):
        PAM._init_(_self, name)
    def displayD(self):
        self._displayName()

obj = PAM_dc('BIA101')
obj.displayD()