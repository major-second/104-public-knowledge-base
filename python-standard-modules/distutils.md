dist意为distribute，即分发你的程序包用的。`setup.py`脚本（装包时用的）就和他有关
- `module 'distutils' has no attribute 'version'`错误：就是`setuptools`版本过高
只需`pip install setuptools==59.5.0`即可（参考[[dependencies]]，版本不是越高越好）