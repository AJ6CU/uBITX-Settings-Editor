from lxml import etree as ET
from globalvars import *

class setters(object):
    def defaultFunc(self, *args):
        print ("Command not recognised:", args[0])

    def set(self, cmd, *args):
        return getattr(self, cmd, self.defaultFunc)(*args)