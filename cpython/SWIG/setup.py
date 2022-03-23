from distutils.core import setup, Extension

# Generated C file: <module>_wrap.c
my_module = Extension('_FOO', sources=['simple_wrap.c'])

setup(name='wtf', description='add func', ext_modules=[my_module],)
