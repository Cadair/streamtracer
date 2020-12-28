import os
import setuptools

# Need to install numpy first
import subprocess
import sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy"])


from numpy.distutils.core import setup, Extension
# Don't want to build the fortran on readthedocs
exts = []
if not os.environ.get('READTHEDOCS', None):
    exts += [Extension(name='streamtracer.fortran.streamtracer',
                       sources=['streamtracer/fortran/Streamtracer.f90'],
                       extra_f90_compile_args=['-fopenmp'],
                       extra_link_args=['-fopenmp']
                       ),
             ]

setup(ext_modules=exts)
