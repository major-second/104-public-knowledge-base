```python
import pickle
with open("1.pkl", "wb") as f:
    pickle.dump(model, f)
```
注意二进制模式`b`
应用
- 对拍！（存成文件然后[[xxd-diff]]）
  - 二分插桩输出文件对拍！看到底哪里开始出了问题不一致