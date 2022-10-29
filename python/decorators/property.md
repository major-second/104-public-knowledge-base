- 例子
```python
class Foo:
    @property
    def bar(self):
        return 'foobar'

print(Foo().bar)
```
- 输出结果`foobar`
- 可以看到，此时`bar`就像是`Foo`类对象的一个attribute，不需要加括号即可调用
- 在逐步运行[[general-principles/debug]]时，就有可能造成意想不到的结果（你以为要进去某个函数了，结果却进到了某个`@property`装饰的property处）
  - 此时退出此栈帧即可，重新按“进入函数”键即可（如vscode的`F11`）
# 应用
- 有时，相当于某种[[5-constraint-satisfaction]]
  - 比如`self.x`和`self.y`始终在变，然后你想让`self.mid`总是得到`self.x+self.y/2`，就可以使用`@property`