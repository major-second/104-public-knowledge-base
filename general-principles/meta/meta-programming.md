> 元编程是指某类计算机程序的编写，这类计算机程序编写或者操纵其他程序（或者自身）作为它们的数据，或者在运行时完成部分本应在编译时完成的工作。
很多情况下与手工编写全部代码相比工作效率更高。
编写元程序的语言称之为元语言，被操作的语言称之为目标语言（百度百科）

## 举例
例如：你在编辑器中写
```python
p = []
for i in range(10):
    p.append(f'print {i}') # 注：用到格式串，这显然是高版本py3

my_interactive_py2_command = \
p[1]$
p[2]$
p[5]$
p[9]

print(my_interactive_py2_command)
```
然后查找`$`替换成` + '; raw_input("Press Enter"); \\\n' + \`，替换完成后保存，再运行保存后的`python3`脚本（本文件夹的`meta_prog_example.py`）
得到一个字符串，是可用于[[interact]]的`python2`片段：即
```python
print 1; raw_input("Press Enter"); \
print 2; raw_input("Press Enter"); \
print 5; raw_input("Press Enter"); \
print 9
```
注意：`print <内容>`和`raw_input()`都说明这是`python2`（`python2`的`input()`不能直接按单个回车）
它使用`; \`，从而适用于在[[interact]]式python中直接粘贴，运行
- 总结
  - 这里使用查找替换（“元语言”。如果你用[[sed]]做的替换那么元语言是shell）修改目标语言python3代码
  - 使用元语言python3生成目标语言python2代码
  - 总共套了两层“meta”