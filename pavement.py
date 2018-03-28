"""
Paver Setup
"""
import os, sys
from paver.easy import options
from paver.setuputils import setup

sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('../task'))

options(
    setup=dict(
        name='study-with-python',
        packages=[],
        version='0.0.0',
        url='https://github.com/murnana/study-with-python/',
        install_requires=['paver','pipenv']
    )
)

from task import create_doc
