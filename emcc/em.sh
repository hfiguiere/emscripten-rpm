#!/bin/sh

EXECUTABLE=`basename $0`
EM_ROOT=/usr/share/emscripten
export PATH=/usr/lib/emscripten/bin:$PATH
export PYTHONPATH=$EM_ROOT
exec $EM_ROOT/$EXECUTABLE $*
