前置
- [[vscode-extensions]]
- [[windows/env-var]]

[参考官网文档](https://robocorp.com/docs/quickstart-guide)
- 首先注册账号
- vscode集成安装：安装指定插件（参考[[vscode-extensions]]）
> Install extensions. Robocorp extensions will take care of all the dependencies you need to develop robots. Install both the **Robocorp Code** and **Robot Framework Language Server** extensions for Visual Studio Code from the Visual Studio Marketplace to get full benefits.

- 命令行工具`rcc`安装
  - [参考](https://github.com/robocorp/rcc#installing-rcc-from-command-line)
  - windows直接找个地方`curl -o rcc.exe https://downloads.robocorp.com/rcc/releases/latest/windows64/rcc.exe`然后把`exe`所在目录加入[[windows/env-var]]的`path`即可
- 装这个有必要，因为vscode集成的不灵活
  - 例如vscode集成的话，你每个robot都不能没有`conda.yaml`
  - 这是[[leaky-abstraction]]