- 前置[[powershell-var]]
- 参考[[12-condition]]
  - 但一些地方有区别
  - 例如
    - 运行结果`$?`是成功为`True`可作为判断条件
    - 而**不能直接**`if (<命令>) {}`用成败做条件！！
    - `if (curl -TimeoutSec 3 https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/.gitignore) {echo 1} else {echo 2}`，如果你没有[[proxy-basics]]就直接啥也不输出，只报错
    - 而同样没有[[proxy-basics]]的情况，`curl -TimeoutSec 3 https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/.gitignore; if ($?) {echo 1} else {echo 2}`输出`2`
  - 但[[ps-process]]又和[[12-condition]]相同，根据`.ExitCode -eq 0`判断成功
- 举例
  - [逻辑运算符](https://learn.microsoft.com/zh-cn/powershell/module/microsoft.powershell.core/about/about_logical_operators?view=powershell-7.3)
  - 简单表达式判断
    ```powershell
    $x = 3; `
    if ($x -lt 5) {
        Write-Output 0
    }; `
    if ($x -lt 5) {
        Write-Output 1
    } else {
        Write-Output 2
    }; `
    if ($x -gt 5) {
        Write-Output 1
    } elseif ($x -eq 3) {
        Write-Output 2
    } else {
        Write-Output 3
    }; `
    $x = "abc"; `
    switch ($x) {
        "ab" { Write-Output 1 }
        "abc" { Write-Output 3 }
        default { Write-Output 5 }
    }
    ```
  - [[ip-address]]是否在国内
    - `if ((curl ipinfo.io | select content | select-string country) -like "*CN*") {}`
  - 文件是否存在（可用于防止[[powershell-basics]] `rm`报错）
    - `if (test-path ...)`