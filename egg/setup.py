#!/usr/bin/env python
#-*- coding:utf-8 -*-

from setuptools import setup, find_packages

setup(
   name = "demo",
   version="0.1.0",
   packages = find_packages(),
   zip_safe = False,

   description = "egg test demo.",
   long_description = "egg test demo, haha.",
   author = "amoblin",
   author_email = "[email protected]",

   license = "GPL",
   keywords = ("test", "egg"),
   platforms = "Independant",
   url = "",
)
