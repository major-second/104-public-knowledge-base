# `foreach`例子
```powershell
foreach ($port in 9999, 10000, 10001)
{
    $proxyServer = "127.0.0.1:$port"
    echo "Trying $proxyServer"
}
```
- `foreach ($user_at_ip in @('git@github.com', 'test@test')`，注意逗号