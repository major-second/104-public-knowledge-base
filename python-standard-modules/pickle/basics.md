- 基本用法
```python
import pickle
with open("1.pkl", "wb") as f:
    pickle.dump(model, f)
```
  - 注意二进制模式`b`，写模式`w`
  - 参考[[file-format]], [[file-handler]]
- 应用
  - 对拍！
    - 即：存成文件然后[[xxd-diff]]
    - 出现问题时，二分，插桩，输出东西对拍，看到底哪里开始不一致
    - 参考[[debug-console]]
  - 作为[[general-principles/cache]]东西的手段，避免反复计算