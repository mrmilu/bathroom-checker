#!/usr/bin/env python3
from setuptools import setup, find_packages
import sys
from pathlib import Path

MODULE_NAME = 'bathroom_checker'
APP_NAME = 'bathroom-checker'

desktop_script = """
[Desktop Entry]
Name={APP_NAME}
Type=Application
Exec=/usr/local/bin/{APP_NAME}
StartupNotify=false
Terminal=false
""".format(**vars())

if sys.platform == "linux":
    try:
        with open("/usr/share/applications/{APP_NAME}.desktop".format(**vars()), "w") as f:
            f.write(desktop_script)
    except Exception:
        print("Enable to create .desktop script. ¿Are you root?")

setup(
    name=APP_NAME,
    description="Tray icon for mrmilu's bathroom-monitor",
    author='Alex Left',
    author_email='aizquierdo@mrmilu.com',
    url='',
    version='0.2',
    entry_points = {
        'console_scripts': ['{APP_NAME}={MODULE_NAME}.{MODULE_NAME}:main'.format(**vars())],
    },
    packages=[MODULE_NAME],
    package_data={MODULE_NAME: ['images/*']},
    include_package_data= True,
    license='GPL-v3',
    long_description=open('README.md').read(),
    install_requires=["pystray", "requests", "pillow"]
)
