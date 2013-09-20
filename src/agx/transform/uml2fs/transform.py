from zope.interface import (
    implementer,
    alsoProvides,
)
from zope.component import getUtility
from node.interfaces import IRoot
from agx.core.interfaces import (
    ITransform,
    ITarget,
)
from node.ext.directory import Directory


@implementer(ITransform)
class UML2FS(object):

    def __init__(self, name):
        self.name = name

    def source(self, path):
        return None

    def target(self, path):
        target = Directory(path)
        # XXX: hook elsewhere, this ignores are self contained buildout related
        target.ignores = [
            'eggs', 'devsrc', 'parts', 'bin', 'develop-eggs', 'var', 'env', 'local', 'lib',
        ]
        alsoProvides(target, IRoot)
        alsoProvides(target, ITarget)
        return target
