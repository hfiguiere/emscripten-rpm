#!/bin/sh

EXECUTABLE=`basename $0`
if [ -z "$EMSCRIPTEN" ]; then
    export EMSCRIPTEN=/usr/share/emscripten
fi
if [ -z "$LLVM" ] ; then
    export LLVM=/usr/lib/emscripten/bin
fi
export PYTHONPATH=$EMSCRIPTEN
exec $EMSCRIPTEN/$EXECUTABLE $*
