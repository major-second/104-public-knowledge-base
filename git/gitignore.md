https://www.jianshu.com/p/a09a9b40ad20
可以参考
比如
```text
__pycache__
*.pkl
path/to/a/folder
```
等等（即：可以匹配文件夹，也可以匹配后缀名，等等）
注意`github`上有一些模板。往往不需要自己纯手动写。
- 注：自己添加`.gitignore`时一定要慎重，不要想当然。举例：以为`.txt`全是数据文件，没有用，但实际上有`pip`的`requirements.txt`非常重要