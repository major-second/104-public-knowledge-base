- 例子
```python
class Foo:
    @property
    def bar(self):
        return 'foobar'

print(Foo().bar)
```
- 输出结果`foobar`
- 可以看到，此时`bar`就像是`Foo`类对象的一个attribute
- 在逐步运行[[general-principles/debug]]时，就有可能造成意想不到的结果（你以为要进去某个函数了，结果却进到了某个`@property`装饰的property处）
  - 此时退出此栈帧即可，重新按“进入函数”键即可（如vscode的`F11`）