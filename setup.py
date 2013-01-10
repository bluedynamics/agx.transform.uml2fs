# Copyright BlueDynamics Alliance - http://bluedynamics.com
# GNU General Public License Version 2
import os
from setuptools import (
    setup,
    find_packages,
)


version = '1.0'
shortdesc ="AGX UML to Filesystem Transform"
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()


setup(name='agx.transform.uml2fs',
      version=version,
      description=shortdesc,
      long_description=longdesc,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: OS Independent',
          'Programming Language :: Python',        
      ],
      keywords='AGX, Code Generator, UML 2 Filesystem Transform.',
      author='BlueDynamics Alliance',
      author_email='dev@bluedynamics.com',
      url=u'https://svn.plone.org/svn/archetypes/AGX',
      license='GNU General Public Licence',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['agx', 'agx.transform'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'agx.core',
          'node.ext.directory',
      ],
      extras_require = dict(
          test=[
            'interlude',
          ]
      ),
      entry_points="""
      # -*- Entry points: -*-
      """)
