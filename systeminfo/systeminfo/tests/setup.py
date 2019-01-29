from setuptools import setup

setup (name="systeminfo",
       version="0.1",
       description="Basic system information for COMP30670",
       url="",
       author="Kieran Daly",
       author_email="kierandaly88@gmail.com",
       licence="GPL3",
       packages=['systeminfo'],
       entry_points= {
           'console_scripts':['comp30670_systeminfo=systeminfo.main:main']
       }
       )