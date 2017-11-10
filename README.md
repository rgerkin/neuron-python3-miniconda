# neuron-python3-miniconda
Installation and testing of the NEURON simulator on OSX using a Miniconda Python 3 installation

[![Build Status](https://travis-ci.org/rgerkin/neuron-python3-miniconda.svg?branch=master)](https://travis-ci.org/rgerkin/neuron-python3-miniconda)

Notes:
- If you get an error like, `dyld: Library not loaded: @rpath/libpython3.5m.dylib`, try `sudo install_name_tool -change @rpath/libpython3.5m.dylib $MC3/lib/libpython3.5m.dylib $NEURON_HOME/bin/nrniv`, where `MC3` is the path to your miniconda3 installation.  
