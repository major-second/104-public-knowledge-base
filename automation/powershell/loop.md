# `foreach`例子
- [[configure]]
```powershell
foreach ($port in 9999, 10000, 10001)
{
    $proxyServer = "127.0.0.1:$port"
    echo "Trying $proxyServer"
    Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings" -Name "ProxyEnable" -Value 1
    Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings" -Name "ProxyServer" -Value $proxyServer
    if (curl -TimeoutSec 3 https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/.gitignore)
    { 
        echo "$proxyServer is usable"
        curl ipinfo.io | select content | Select-String country
        $using_proxy = 1
        break
    }
}
```