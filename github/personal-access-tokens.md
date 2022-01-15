`git clone`private库，要求登录。
以前，对于`git`命令行，可以直接输入账户密码验明自己身份。
但是为了安全考虑，`git`现在已不允许命令行`clone`时账户密码登录。必须先生成personal access tokens (PATs)，再在密码处改填token. #git
具体步骤
1. 前提：拥有github账号并验证邮箱
2. github右上角头像 - Settings - Developer settings - Personal access tokens - Generate new token, 按提示生成token，复制住并自己妥善保存
    1. 注意过程中要给token赋予适当的权限和有效期
3. `git clone`验证身份时，账号还是填账号，密码处改填生成的token即可