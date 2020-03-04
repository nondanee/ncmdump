# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

try:
    from pip._internal.req import parse_requirements
except ImportError:
    from pip.req import parse_requirements

requirements = parse_requirements(
    os.path.join(os.path.dirname(__file__), 'requirements.txt'),
    session = False
)

setup(
    name = 'ncmdump',
    version = '0.1.0',
    description = 'netease cloud music copyright protection file dump',
    url = 'http://github.com/nondanee/ncmdump',
    author = 'nondanee',
    author_email = 'iminezn5656@outlook.com',
    license = 'MIT',
    keywords = ('ncm', 'netease cloud music'),
    packages = find_packages(),
    platforms = 'any',
    zip_safe = False,
    python_requires = '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    install_requires = [str(requirement.req) for requirement in requirements],
    entry_points = {
        'console_scripts': [
            'ncmdump=ncmdump.app:main'
        ]
    }
)