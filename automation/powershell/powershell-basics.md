# 概述
- 开始菜单或vscode下方都有powershell
- 相当于linux的终端。可以执行命令
  - 不过时至2022还没linux的命令行好用
  - 不客气地说，win命令行，就是垃圾
# 运行
- 没有权限？参考[[administrator-powershell]]，以及其中的`ExecutionPolicy`相关设置命令
- 不能双击运行？从而[[windows-link]]也不方便一个快捷键运行？[[file-format]]打开方式选择`C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe`这种东西
# 基础命令
- `help <命令>`，`gal <命令>`看命令的基本信息，例如`gal rm`
  - 比如`rm`其实是`Remove-Item`，`ls`其实是`Get-ChildItem`
  - 可以看出Powershell的命名格式：大写单词，`-`连接动词和名词
  - `gal`自身是`Get-Alias`，2333
  - 很多命令是为了让linux的人好用所以做了alias
  - 你可以`gal`一下`mv cp ls rm cat diff cd echo sleep`等
- `New-Item`
  - `New-Item -type Directory`相当于了`mkdir`
  - 不加参数就相当于了`touch`
  - `New-Item`的alias通过`help`查到是`ni`
- `scp, ssh, curl, git`等可以用
  - 不过可能有一些特点可能和linux中的不同，毕竟还是不正宗！
  - 例如
    - 路径的`~`记号表示home可能用不了了
    - `gal curl`其实是`Invoke-WebRequest`
      - 参数列表和linux正宗的[[curl-wget]]中的`curl`不一样
      - 比如`-Proxy`临时[[configure-proxy]]而不是`-x`
      - 比如有些电脑上加上`-UseBasicParsing`才能用
    - [[https-ssh]]有提到`ssh-keygen.exe`特性也和linux下`ssh-keygen`不完全一样
- `select`字段
  - `curl https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/.gitignore | select statuscode`，输出`200`这种
  - [[reinstall-app]]中提到了
# 基础技巧
- 编辑技巧：可以用上下方向键看历史，`Tab`补全等
  - `*.zip`再`Tab`这样还能自动找匹配来补全，非常好用
  - 右键粘贴
- 换行不是`\`，而是<code>&#96;</code>
  - 这和[[11-basic-scripting-partA]]不同
- `;`还是可以分割多条命令
  - 所以[[11-basic-scripting-partA]]常见的`; \`这里就是<code>; \`</code>
  - 举例
```powershell
echo 1 `
echo 2; `
echo 1; `
echo 2
```
输出
```text
1
echo
2
1
2
```
- `$PSScriptRoot`直接取出脚本所在路径，方便设置相对路径等
  - 注意运行时的路径不一定等于`$PSScriptRoot`
- 双引号内部，转义[[escape]]也是 <code>&#96;</code>
  - 例如 <code>echo "\`""</code>这样输出`"`
  - 例如 <code>echo "\`\$"</code>这样输出`$`
  - 内部`$某某`使用windows的变量，<code>\`\$</code>才是真的`$`
  - [[wsl-command]]经常用到
  - 举例（这里需要你掌握[[6-env]], [[windows/env-var]], linux的[[escape]]等）
    - <code>echo "echo '\`\$HOME'; echo \`"\`\$HOME\`"; echo '\$HOME'; echo \`"\$HOME\`""</code>
      - 得到<code> echo '\$HOME'; echo "\$HOME"; echo 'C:\Users\windowsusername'; echo "C:\Users\windowsusername"</code>
      - 也就是
        - `$HOME`被直接替换成windows的[[windows/env-var]]
        - <code>\`\$HOME</code>变成`$HOME`，从而可以取出linux的[[6-env]]
    - <code>wsl -e bash -c "echo '\`\$HOME'; echo \`"\`\$HOME\`"; echo '\$HOME'; echo \`"\$HOME\`""</code>
      - 依次输出
        - `$HOME`
        - `/root`
        - `C:\Users\windowsusername`
        - `C:Userswindowsusername`
  - 总之复杂条件下双引号灵活，内部可以有单双引号反引号美元等等，顶多转义
- 单引号
  - 内部不能转义，不能 <code>echo '&#96;''</code>
  - 但是<code>echo '\`\$"\`'</code> 可以原样输出<code>\`\$"\`</code>，也就是内部除了不能单引号，其它什么都好
  - 总体上和双引号是[[aggregation]]关系，有时互为[[workaround]]