#!/usr/bin/env python
import os.path
import re
from setuptools import setup

setup(
	name="virtualenv-bin",
	version="0.9.1",
	author="Devon Jones",
	author_email="devon.jones@gmail.com",
	url="https://github.com/devonjones/virtualenv-bin",
	license = "Apache",
	scripts = [
		"bin/venvbin",
		"bin/venvsymlinks",
		"bin/venvlaunch"],
	description = "Set of bash scripts that make bins installed in virtualenvs useful elsewhere.",
	long_description = "\n" + open("README.rst").read(),
)

