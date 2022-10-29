天天都说“组合优于继承”，不要动辄类继承，那不继承怎么办？
举例：[[gym/wrapper]]，[[dataset]]当中都常见一种典型解决方案：
- `__init__`加入`unwrapped_obj`形参
- 写`self.unwrapped_obj = unwrapped_obj`
- `self`的方法使用`self.unwrapped_obj`的方法。例如
```python
def reset(self):
    return self.unwrapped_env.reset()
```
```python
def __getitem__(self, index):
    return self.unwrapped_list[index]
```