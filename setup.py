"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['main.py']
DATA_FILES = ['util', 'resource/pyGNSSTime.icns']
OPTIONS = { 'iconfile' : 'resource/pyGNSSTime.icns', 
            'plist' : {
                'CFBundleName' : 'pyGNSSTime',
                'CFBundleDisplayName' : 'pyGNSSTime',
                'CFBundleVersion' : '1.0.0',
                'CFBundleIndentifier' : 'pyGNSSTime_v1.0.0',
                'NSHumanReadableCopyright' : 'Copyright @ 2024 JIANG Tingwei. All rights reserved.'
            }
          }

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
