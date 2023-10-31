- 参考
    - [[powershell-var]]
    - [[windows/env-var]]
- 格式`env:...`
- [[CRUD]]
  - 直接`$env:<名字>`可以查询。和[[windows/env-var]]查询结果相同
    - 如
      ```powershell
      > $env:windir
      C:\Windows
      ```
  - 直接`$env:<k> = "<v>"`改动
    - 改动成空就是删除
    - 注意这个和[[6-env]]不同，需要`$`开头
- 应用
  - [[configure-proxy]]
    - `$env:http_proxy = "http://127.0.0.1:<端口号>"`
  - `$env:UserName`得到用户名