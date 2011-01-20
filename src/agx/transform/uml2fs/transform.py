# Copyright BlueDynamics Alliance - http://bluedynamics.com
# GNU General Public License Version 2

from zope.interface import implements
from zope.interface import alsoProvides
from zope.component import getUtility
from zodict.interfaces import IRoot
from agx.core.interfaces import ITransform
from agx.core.interfaces import ITarget
from node.ext.directory import Directory

class UML2FS(object):
    
    implements(ITransform)
    
    def __init__(self, name):
        self.name = name
    
    def source(self, path):
        return None
    
    def target(self, path):
        target = Directory(path)
        alsoProvides(target, IRoot)
        alsoProvides(target, ITarget)
        return target