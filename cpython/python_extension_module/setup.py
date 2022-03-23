from distutils.core import setup, Extension

foo_module = Extension('foo', sources=['simple.c'])

setup(name='wtf', description='add func', ext_modules=[foo_module])
