# `foreach`例子
```powershell
foreach ($port in 9999, 10000, 10001)
{
    $proxyServer = "127.0.0.1:$port"
    echo "Trying $proxyServer"
}
```