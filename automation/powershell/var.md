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
## 普通
- `$x = 5; echo $x`
- shell中是`x=5`哈哈，区别一下