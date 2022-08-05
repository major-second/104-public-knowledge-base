## 前置
- 拥有github账号并验证邮箱
## 用户名和token的生成
`git clone`github上private库（或者其它涉及私人的操作）时，要求登录
以前，对于`git`命令行操作，可以直接输入账户密码验明自己身份
但是为了安全考虑，github现在已不允许命令行`clone`时账户密码登录
现在应该：
1. github右上角头像 - Settings - Developer settings - Personal access tokens - Generate new token, 按提示生成token，复制并自己妥善保存
    - 注意过程中要给token赋予适当的权限和有效期
2. `git clone`验证身份时，账号还是填账号，密码处改填生成的token即可
## 取消credential helper保存
push一步遇到问题：remote: repository not found
可能是credential helper的问题，即git自动记住了以前输过的用户名密码，但是以前的用户名密码不是我这个仓库需要的用户名密码！
使用`git config --global --unset credential.helper`取消保存
## vscode相关
- vscode记住的authentication可能也会导致问题，参考[[vscode/settings]]中有关`git.terminalAuthentication`条目
- 这种出错的典型示例
```text
Missing or invalid credentials.
Error: connect ECONNREFUSED
```
- [[push-pull]]没反应，但`git clone`公开repo没问题，也可能是这种情况