# 6-env
- `source`和直接运行不同
  - 直接运行的`export key=value`只影响子进程，没法给当前进程导入变量。`source`或`.`可以
- 在[[shell-type]]用不了`source`时的[[workaround]]：`eval $(cat my-script.sh)`，是[[meta-programming]]
## 6.7 数组变量
- 定义：`k=(v1 v2 v3)`
- 取用首位：`echo $k`或`echo ${k[0]}`
- 取用`v3`：`echo ${k[2]}`
- 读整体：`echo ${k[*]}`
- 删改
  - `k[2]=v4`
  - `unset k[1]`
  - 注：此时比较坑，`echo ${k[*]}`是`v1 v4`，但`v4`对应的是2号位，即`echo ${k[2]}`得到`v4`
  - 总之shell数组挺坑的，除非你确认知道怎么用，否则别用
- 清空整体：`unset k`
- 注：[[17-function]]中可以使用数组，但也挺坑的，参考[[17-function]]
- 注：[[zsh]]的数组和bash开始是1还是0不同……坑死了
  - 可以[[12-condition]]，参考[[zsh]]