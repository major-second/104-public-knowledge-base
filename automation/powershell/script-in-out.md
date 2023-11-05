# 输入
- 输入参数
  - 需要你`.ps1`脚本开头声明`param($name1, $name2)`这样，没声明不能用
  - 之后也是`$name1`使用
  - 对比bash[[17-function#17.3]]：直接`echo $1`不需声明
- `$MyInvocation.MyCommand.Path`类似于bash的`$0`，得到脚本自身路径（这个倒是直接可用）
# 输出
- `exit`
- `exit 0`成功，`exit 1`失败，和[[11-basic-scripting-partB]]一样
- `$?`则`False`对应失败，`True`对应成功，而**不是返回值直接做类型转换**！
- `$?`可以作为[[condition]]的条件