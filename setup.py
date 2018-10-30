#!/usr/bin/env python
# -*- coding: utf-8 -*-

r''' Copyright 2018, SigDev

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License. '''

from setuptools import setup, find_packages
from os.path import join, dirname, realpath
import keywords_b2b

setup(name=keywords_b2b.__name__,
      version=keywords_b2b.__version__,
      packages=find_packages(exclude=[r'example']),
      description=r'Keywords CSV generator',
      long_description=open(join(dirname(__file__), r'README.rst')).read(),
      author=keywords_b2b.__author__,
      license=keywords_b2b.__license__,
      url=r'http://github.com/sigdev2/keywords_b2b',
      keywords=r' '.join([
        r'excel', r'csv', r'python', r'keywords', r'generator', r'combinations', r'b2b', r'context', r'advertising'
        ]
      ),
      classifiers=[
        r'Environment :: Console',
        r'Intended Audience :: End Users/Desktop',
        r'Intended Audience :: Information Technology',
        r'License :: OSI Approved :: Apache Software License',
        r'Operating System :: OS Independent',
        r'Programming Language :: Python',
        r'Topic :: Software Development',
        r'Topic :: Software Development :: Libraries :: Python Modules',
        r'Topic :: Utilities',
        r'Topic :: Office/Business',
        r'Programming Language :: Python :: 2.6',
        r'Programming Language :: Python :: 2.7',
        r'Programming Language :: Python :: 3',
        r'Programming Language :: Python :: 3.2',
        r'Programming Language :: Python :: 3.3',
        r'Programming Language :: Python :: Implementation :: PyPy',
        ],
      install_requires=[],
      entry_points={
        r'console_scripts': [
          r'keywords_b2b = keywords_b2b.__main__:main',
          ]
      },
      zip_safe=False
)
