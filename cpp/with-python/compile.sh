EXT_SUFFIX=$(python3-config --extension-suffix)
INCLUDES=$(python3 -m pybind11 --includes)
rm ./*.so
c++ -O3 -Wall -shared -std=c++11 -fPIC $INCLUDES my_sum.cpp -o my_sum$EXT_SUFFIX
python test.py