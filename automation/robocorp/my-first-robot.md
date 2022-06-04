前置
- [[robocorp/installation]]
- 可能需要[[configure]]代理

步骤
- [官方参考文档](https://robocorp.com/docs/setup/robot-structure)
- 举例：最简单的
`git clone https://github.com/robocorp/example-google-image-search.git`下来，vscode打开此库
    - 此时对于windows系统自动出现[此troubleshooting](https://robocorp.com/docs/troubleshooting/windows-long-path)，照做即可
    - 照做重启之后可以进入下一步
- 左侧出现robocorp图标
  - 点它，现在开始加载![](my-first-robot.png)
  - 过程可能很慢（主要是下载装包等）
- 挂好代理[[configure]]确保谷歌能上，然后vscode左侧robocorp图标 - ![](start.png)
- 运行成功效果：
  - 下方有提示
  - 打开（可能用浏览器等）运行成功生成的`log.html`，可以找到猫猫图片![](cat.png)