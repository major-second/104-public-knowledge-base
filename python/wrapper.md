天天都说“组合优于继承”，不要动辄类继承，那不继承怎么办？
举例：[[gym/wrapper]]，[[dataset]]当中都常见一种典型解决方案：
- `__init__`加入`wrapped_obj`形参
- 写`self.wrapped_obj = wrapped_obj`
- `self`的方法使用`self.wrapped_obj`的方法。例如
```python
def reset(self):
    return self.wrapped_env.reset()
```
```python
def __getitem__(self, index):
    return self.wrapped_list[index]
```