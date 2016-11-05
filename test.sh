echo "begin script"
export PYTHONPATH=$PYTHONPATH:$TRAVIS_BUILD_DIR/Python3-Core/src/generated
export PYTHONPATH=$PYTHONPATH:$TRAVIS_BUILD_DIR/Python3-Core/src/main
nosetests Python3-Core/src/test/prompto/
export PYTHONPATH=$PYTHONPATH:$TRAVIS_BUILD_DIR/Python3-Runtime/src/main
$export PYTHONPATH=$PYTHONPATH:$TRAVIS_BUILD_DIR/Python3-Core/src/test
nosetests /Python3-Runtime/src/test/
echo "end script"
