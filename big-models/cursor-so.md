- 参考
  - [[chatgpt]], [[waitlists]]
  - [[git-basics/basics]]的`git add`很有帮助
- [cursur.so](https://www.cursor.so/)
- 前置
  - [[openai-account]]，[[openai-api]]
    - （在上方最小化按钮旁边的齿轮处加）
  - 了解[[vscode]]有帮助
    - 可能可以导入部分vscode事物，例如[[vscode-extensions]]
    - 但是cursor毕竟还不成熟，可能有些[[vscode-extensions]]不如原版上线快，原版vscode能用这里不能用
# 概述
- 生成和交互代码
  - 官方指南
    ```text
    # 1. Try generating with command K on a new line. Ask for a pytorch script of a feedforward neural network
    # 2. Then, select the outputted code and hit chat. Ask if there's a bug. Ask how to improve.
    # 3. Try selecting some code and hitting edit. Ask the bot to add residual layers.
    # 4. To try out cursor on your own projects, go to the file menu (top left) and open a folder.
    ```
  - 最常用快捷键
    - `Ctrl+K` Edit
      - 在已有代码基础上编辑
      - 把注释[[comment]]变成代码
      - 代码重构
    - `Ctrl+L` (New) Chat
      - 解说，闲聊，不改变当前代码
      - 但也可以（迭代）生成代码块，复制过来
      - [[refresh]] 了 chat thread
    - `Ctrl+退格` 取消
    - `Ctrl+Enter` 接受
      - 如果不想全部接受，可以先`git add`这个文件，然后接受之后对比新旧版本，选择性接受
  - 可以作为开发环境打开文件夹等
  - 被收入[[editor-index]]
  - 当然免费的会达到maximum capacity，这时就需要[[aggregation]]
# 用例
- 不一定是代码相关！比如选中`# 皮带 电蚊拍 洗牙器 自行车头盔`，`Ctrl + K`，翻译成英文，输出`# Belt, electric mosquito swatter, dental scaler, bicycle helmet`
# 注意
- troubleshooting: [参考这个](https://zhuanlan.zhihu.com/p/639956119)，可能程序员写反了东西，所以需要把 OpenAI API 关掉
- 记得复制提示（避免intermittent的服务器错误）
- 生成后可以
  - accept, reject
  - 手动删除手动修改，而不简单接受或拒绝
- 可以先写[[comment]]或部分代码，要求它补全
- 可以后台运作
- [[vscode-keyboard-shortcuts]]
  - 有些快捷键在这里被占用了
    - 比如`Ctrl+K` `Ctrl+Y`
  - 还原：从`Ctrl+Y`变成`Ctrl+Shift+Z`