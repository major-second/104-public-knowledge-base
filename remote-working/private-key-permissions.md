- 前置
    - [[generate-key-pair]]
    - [[private-key-私钥]]
- 私钥权限太开放会不给你用
- Linux
  - `chmod 600`它
  - [[7-permissions]]
- Windows
  - GUI
     - `右键-Properties-Security-Advanced-Disable inheritance-去除所有继承的权限`
     - 然后去除所有权限
     - 然后给当前用户加上读权限（即刚刚Advanced界面那里`Add-Select a principal-Enter the object name to select处输入用户名-OK，自动出现Principal编号-一路OK`）
  - 或[[powershell-acl]]