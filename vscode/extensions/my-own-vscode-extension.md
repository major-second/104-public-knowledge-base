# 前置
- [[yeoman]]中相应的[[yeoman-generator]]
- `npm install -g @vscode/vsce`
- [[other-hubs]]中[Azure DevOps](https://azure.microsoft.com/services/devops/)
  - 创立organization
  - 获得[[personal-access-tokens]]用于`vsce login <name>`命令
# 本地
- 到你想要的文件夹
- Use `yo code` command to generate a basic extension project
  - 根据提示操作，然后看到新产生文件夹
  - 过程中也指定了插件名字，之后用到
  - Open the project folder with VS Code
    - 可能在`yo code`后根据提示自动完成了
    - 注：之后每次想调试也需要先打开相应文件夹，否则会出现类似于`python`中[[where-from]]的相关问题：找不到对应`module`
- vscode窗口中选择`*.js`文件
- press F5 to run the extension in a new window
  - 参考[[vscode-debug-js]]，不需插件，直接debug
  - 这个新窗口中Test your extension by running the Hello World command from the Command Palette (Ctrl+Shift+P) in the new window
# publish
- 看文档
  - [官网](https://marketplace.visualstudio.com/)注册账号
  - [vscode页面](https://marketplace.visualstudio.com/vscode)
  - 点publish extension
  - 按指示操作，过程中参考 [这个文档](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)
- 确保已经[注册publisher](https://marketplace.visualstudio.com/manage)
  - 并和刚刚[[personal-access-tokens]]一个[[general-principles/account]]
  - 终端`vsce login <name>`，输入tokens
- 到extension文件夹
  - 刚刚[[yeoman-generator]]自动生成了东西，你需要编辑一下
    - README随便改一下
    - 为了防止[[warning]]烦人，可以
      - 加入`repository`属性
      - 加入`license.md`
    - `package.json`中
      - 加入一行`publisher": <publisher_name>,`
      - 改[[compatibility]]声明
        - `"engines"`
          - `"^1.74.2"` is equivalent to `">=1.74.2 <2.0.0"`
          - 参考[[version#常识]]
        - ```json
          "devDependencies": {
            "@types/vscode":
          ```
          这里也要改
        - 改完需要该文件夹`npm install`刷新
      - （可能）更新`version`字段，不能和以前一样
  - `vsce publish`
- 之后
  - 可能需要过几分钟，并[[refresh]] vscode，待检查是不是这样
    - 可能成功之后有邮件通知
  - 你的插件可以搜到，是`<publisher_name>.<extension_name>`形式
  - 注意刚刚[本地生成时](#本地)已经生成了`extension_name`