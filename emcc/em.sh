#!/bin/sh

EXECUTABLE=`basename $0`
EM_ROOT=/usr/share/emscripten
export PYTHONPATH=$EM_ROOT
exec $EM_ROOT/$EXECUTABLE $*
