- 安装
```sh
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg
sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'
sudo apt update
sudo apt install code
```
- 安装[[extensions/general]]：`code --install-extension <插件ID>`
  - `ID`查看方法：如图右键齿轮![](extension-id.png)
- 列出[[extensions/general]]：`code --list-extensions`
- 查看版本：`code --version`
- `root`身份启动：`code --no-sandbox --user-data-dir <文件夹>`