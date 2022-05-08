# 17.1
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
这不能少，太丑了！
联想[[11-basic-scripting-partB]]中的`expr 2 \* 3`
# 17.2
- 返回值：默认最后一条的返回值，参考`$?`，[[11-basic-scripting-partB]]
- `return`：数值范围有限！而且原始目的不是那种“数学函数”返回值。是标记是否正常运行之类的。
- 使用`echo`输出，使用`$()`取用：注意这样一来函数中不能用其他`echo`，要用`read -p`
# 17.3
- 使用`$#, $1, $2`等等取用传入参数（`$0`另有他用，参见[[14]]）
- 不需要写“形参”
- 内层遮蔽外层的`$1`

待续todo