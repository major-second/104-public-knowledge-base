- 前置：了解[[escape]]
- `r`表示忽略转义，直接该是啥就是啥。常用于需要很多`\`符号时，例如[[text]]中数学文本
```python
>>> print('\n')


>>> print(r'\n')
\n
```
- 注意：`print()`自带一个空行，所以没有使用r-string的`\n`就是两个空行