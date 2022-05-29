```python
>>> a
{'b': '${c}:${d}'}
>>> OmegaConf.merge(a,{'c':1,'d':2})
{'b': '${c}:${d}', 'c': 1, 'd': 2}
>>> a = OmegaConf.merge(a,{'c':1,'d':2})
>>> a.b
'1:2'
```
- 在vscode debugger中，展开输出的`{'b': '${c}:${d}', 'c': 1, 'd': 2}`可以看到`b`被interpolate了
- interpolate实际上有[[lazy]]的效果：也就是暂时还不给出值，但我已经知道要去哪里找了
- 注意`.`，`..`，`...`等表示相对路径，而不加的表示绝对路径