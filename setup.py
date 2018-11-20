#!/usr/bin/env python3
from setuptools import setup, find_packages
import sys
from pathlib import Path


desktop_script = """
[Desktop Entry]
Name=bathroom_checker
Type=Application
Exec=/usr/local/bin/bathroom-checker
StartupNotify=false
Terminal=false
"""

if sys.platform == "linux":
    try:
        with open("/usr/share/applications/bathroom-checker.desktop", "w") as f:
            f.write(desktop_script)
    except Exception:
        print("Enable to create .desktop script")

setup(
    name='bathroom_checker',
    description="Tray icon for mrmilu's bathroom-monitor",
    author='Alex Left',
    author_email='aizquierdo@mrmilu.com',
    url='',
    version='0.1',
    entry_points = {
        'console_scripts': ['bathroom-checker=bathroom_checker.bathroom_checker:main'],
    },
    packages=["bathroom_checker"],
    package_data={'bathroom_checker': ['images/*']},
    include_package_data= True,
    license='GPL-v3',
    long_description=open('README.md').read(),
    install_requires=["pystray", "requests", "pillow"]
)
