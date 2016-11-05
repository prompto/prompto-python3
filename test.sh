export PYTHONPATH=$PYTHONPATH:$TRAVIS_BUILD_DIR/Python3-Core/src/generated
export PYTHONPATH=$PYTHONPATH:$TRAVIS_BUILD_DIR/Python3-Core/src/main
nosetests --exe Python3-Core/src/test/prompto/
export PYTHONPATH=$PYTHONPATH:$TRAVIS_BUILD_DIR/Python3-Runtime/src/main
export PYTHONPATH=$PYTHONPATH:$TRAVIS_BUILD_DIR/Python3-Core/src/test
nosetests --exe Python3-Runtime/src/test/
