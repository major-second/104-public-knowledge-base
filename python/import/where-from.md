想知道目前用的包来自哪里？
- `pip list`（如果表太长就后面再`| grep <包名>`）
如果有显示本地目录，那就来自本地
- `python -c "import sys; print(sys.path)"`，也可以看到所有用到的路径。不妨用这个和`pip list`的结果做对照

应用：import时，参考这些路径来写。比如`sys.path`里有`foo`，`foo`下属`bar.py`，就可以直接`from bar import ...`