UML2FS Transform
----------------

::
    >>> import os
    >>> import tempfile
    >>> tempdir = tempfile.mkdtemp()
    >>> targetpath = os.path.join(tempdir, "target")
    >>> from agx.core.interfaces import ITransform
    >>> from zope.component import getUtility
    >>> transform = getUtility(ITransform, name="uml2fs")
    >>> transform.source(None)

    >>> transform.target(targetpath)
    <Directory object '/.../target' at ...>
