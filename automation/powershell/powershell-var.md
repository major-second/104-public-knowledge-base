前置
- [[powershell-basics]]
- 了解[[windows/env-var]]

内容
## 环境变量`env:...`
- 环境变量都是字符串
- 直接`$env:<名字>`可以查询。和[[windows/env-var]]查询结果相同
  - 如
```powershell
> $env:windir
C:\Windows
```
- 直接`$env:<k> = "<v>"`改动
  - 改动成空就是删除
  - 注意这个和[[6-env]]不同，需要`$`开头
- 应用：`$env:http_proxy = "http://127.0.0.1:<端口号>"`
## 普通变量
- `$x = 5; echo $x`
  - [[11-basic-scripting-partA#11.4 使用变量]]中是`x=5`
  - 哈哈，区别一下
- `%SystemRoot%`这种也可以取出
- `$PSScriptRoot`直接取出脚本所在路径，方便设置相对路径等
  - 注意运行时的路径不一定等于`$PSScriptRoot`