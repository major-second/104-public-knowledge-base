[toc]
- 参考
  - [[code-data]]
  - [[naming#命名有时是相对的]]
## 定义
> 元编程是指某类计算机程序的编写，这类计算机程序编写或者操纵其他程序（或者自身）作为它们的数据，或者在运行时完成部分本应在编译时完成的工作。
很多情况下与手工编写全部代码相比工作效率更高。
编写元程序的语言称之为元语言，被操作的语言称之为目标语言（百度百科）
## 坏处
- 容易出错，无法[[general-principles/debug]]
  - 因为代码动态生成，没法分析
- [[escape]]麻烦
## 举例
- 通过代码生成代码显然属于元编程
  - 例如[[subprocess]]中用`python`生成、处理、运行`shell`命令
- 命令行中`python -c <代码>`，`bash -c <代码>`等，如果`<代码>`自身就经过处理等等，那就属于元编程
- 把变量名`foo`和字符串`foo`关联起来也属于
  - 例如[[register-classes]]自动由字符串找到类名
  - [[call-hook]]自动由字符串找到方法名
## 具体举例
### `python -> markdown`
- 由于`markdown`是标记语言，所以自动生成markdown文档也勉强算元编程吧。而且这是比较简单的例子
- 本例子前置知识[[file-format]]，[[enhanced]]，[[common-func]]，[[f-string]]
```python
''.join([f'\t- 长度：${l}$\n![](length-{l}.jpg)\n' for l in lengths])
```
- 可以看到，用[[f-string]]的大括号结合推导式`for`生成了一个列表，然后拼接在一起可得到想要的字符串
- 使用了<code>\t-&nbsp;</code>的“二级item”，`$$`包裹数学公式，`![](<图片名.jpg>)`等常见markdown功能，有的还是[[enhanced]]功能
- 之后只需`open`一个`.md`文件写进去即可
### `shell -> shell`
#### 例1
- shell中最简单的元编程例子
  - `a=b; b=c; echo ${$a}`
    - 然而直接运行这个会报错`bad substitution`
  - 那就`a=b; bash -c "b=c; echo \$$a"`
#### 例2
- [[pip]]和[[conda/commands]]要求格式不同。一个是`<包名>==<版本>`，一个是`<包名>=<版本>`
- 所以可以在一个`.txt`中写`<包名>$<版本>`，然后用`pip install ${module/\$/==}`之类的
- 相当于用`shell`的`${//}`语法编辑了`shell`命令
- `shell`这种语言的特点就是易于编辑字符串，易于使用元编程
### `shell -> python3 -> python2`
- 本例子前置知识[[sed]]，[[f-string]]，[[version]]，[[interact]]
- 你在编辑器中写
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
- 然后查找`$`替换成` + '; raw_input("Press Enter"); \\\n' + \`，替换完成后保存，再运行保存后的`python3`脚本（本文件夹的`meta_prog_example.py`）
- 得到一个字符串，是可用于[[interact]]的`python2`片段：即
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