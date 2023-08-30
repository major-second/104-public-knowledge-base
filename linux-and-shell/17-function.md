前置：
- [[6-env]]
- [[11-basic-scripting-partB]]
参考
- [[alias]]
## 17.1
```sh
function name {
    commands
}
```
或
```sh
name() {
    commands
}
```
注意`function name {`大括号前空格！
- 这空格不能少，是不是很让人恼火，但shell就是这么烦
- 联想[[11-basic-scripting-partB]]中的`expr 2 \* 3`，是不是也很丑，也要求空格不能省
## 17.2
- 函数返回值
  - 默认为最后一条命令的返回值，参考`$?`，[[11-basic-scripting-partB]]
  - 手动指定`return`：数值范围很有限！
    - 返回值的原始目的本来就不是那种“数学函数”的返回值（什么`return a+b`这种感觉肯定不是）
    - 是标记是否正常运行，以及错误类型等
  - `return 某`和`exit 某`完全不同
    - 如果`exit`，那么会导致直接退出终端，而不是仅退出这个函数
    - 相当于很多时候的按`Ctrl+D`
- 那如果需要返回一个长字符串怎么办？
  - 函数中使用`echo`输出
  - 函数外使用`$()`取用（对比刚刚做法是：先`func`运行完，再使用新的一句`$?`取用）
  - 注意这样一来函数中不能用其他`echo`
    - 比如要用`read -p`给出读取东西的prompt（提示）
      - 类比python的`input('prompt')`
    - 而不能用`echo`再`read`的方法给prompt
- `return`用例

```sh
func() {
    return 3
}
func # 单独运行，返回值被自动记录
echo $?
```
- `$()`用例

```sh
func() {
    echo 33333333
}
echo $(func) # $()包裹运行得到结果
```
## 17.3
- 使用`$#, $1, $2`等等取用传入实参
  - `$0`是函数名（或脚本文件名自身）
    - 所以脚本中`cd $(dirname $0)`可以到脚本所在目录
    - 很多时候这是运行脚本第一步[[reduction]]
    - 类似[[powershell-var]]中`$PSScriptRoot`
  - `$#`是参数个数
- 不需要写“形参”，就可以直接用`$1, $2`等
  - 和powershell的[[script-in-out]]形成区别！
- 如果出现`.sh`脚本中定义了函数，你调用脚本时赋予了1个实参`a`，但脚本中调用函数没有赋予实参，那么函数中不可以用`$1`获得实参`a`
  - 但脚本中，函数外处，定义的全局变量在函数内可以访问
  - 也就是**自动产生的`$1`这种变量**和**手动指定`<name>=<value>`后的`$name`这种变量**两类东西行为完全不同！
- 如果函数内外有同名变量，默认是全局的
  - 但可以使用`local`关键字使得其变为局部
    - 可以先`local <name>`再赋值
    - 也可以一步到位`local <name>=<value>`
  - 这思想和python恰好相反
    - python里有`nonlocal`
    - 只有指定`global`或`nonlocal`才是非局部
## 17.4
- 先阅读参考[[6-env]]
- 和[[6-env]]中相同，不能直接把`$数组名`作为实参！
- 必须把`${数组名[*]}`作为实参，从而有多个实参，然后在函数内可以`$@`取得所有实参
- 举例

```sh
func() {
    echo $#
    echo $@
}
k=(v1 v2 v3)
unset k[1]
echo $(func $k)
echo $(func ${k[*]})
```
- 进阶：刚刚相当于拆成单个变量传进了函数，那我函数中又可以构造回数组
  - 回忆[[6-env]]：用括号包裹得到数组
- 举例

```sh
func() {
    echo $#
    local_array=($(echo $@))
    echo ${local_array[1]}
}
k=(v1 v2 v3)
unset k[1]
echo $(func $k dummy)
echo $(func ${k[*]})
```
输出结果
```text
2 dummy
2 v3
```
- 注意：这里涉及到了[[6-env]]中删除数组中一个值可能造成的大坑
  - 函数外，`k`长度（即使在`unset k[1]`后）一直是3，但传进去之后构造的`local_array`长度是2
  - 再次说明了数组不太好用，容易出坑
- 同理：想返回数组，也应当`echo`一个`${<函数内数组名>[*]}`，然后函数外取出，再括号包裹，构造数组
- 一个实用技巧：函数中`shift 2`把前两个实参丢弃，然后用`$@`可取出剩余所有实参。举例

```sh
func() {
    shift 2
    echo $@
}
func 1 2 3 4 5
```
输出`3 4 5`
- 应用：利用[[echo]]，带颜色地测试命令
```sh
function test-command {
    echo -e \\033\[32m $@ \\033\[0m
    echo -e \\033\[35m $($@) \\033\[0m 
}
```
- 这里`\[`是为了兼容`bash`和[[zsh]]，在bash中是trivial的转义
## 其它
- 一个地方写函数，其它地方用？需要`source`命令，参考[[6-env]]
- 名字可能遮蔽，所以命名要小心。这个不像python那么clean
  - `function a { b=1; echo $b }; b=2; echo $b; a; echo $b`