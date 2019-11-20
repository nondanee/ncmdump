from setuptools import setup, find_packages
import sys

py_version = sys.version_info[:2]

if (3, 0) < py_version < (3, 4):
    raise RuntimeError('On Python3, ncmdump requires Python 3.4 or later')

setup(name='ncmdump',
      version='0.1.0',
      description='netease cloud music copyright protection file dump',
      url='http://github.com/nondanee/ncmdump',
      author='nondanee',
      author_email='iminezn5656@outlook.com',
      license='MIT',
      keywords=('ncm', 'netease cloud music'),
      packages=find_packages(),
      include_package_data=True,
      platforms="any",
      zip_safe=False,
      install_requires=['argparse', 'pycryptodome', 'mutagen'],
      entry_points={
          'console_scripts': [
              'ncmdump = ncmdump.ncmcli:main',
          ]
      }
      )
