- 参考[[chatgpt]], [[waitlists]]
- [cursur.so](https://www.cursor.so/)
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
      - 或注释[[comment]]变成代码
      - 代码重构
    - `Ctrl+L` Chat
      - 解说，闲聊，不改变当前代码
    - `Ctrl+退格` 取消
    - `Ctrl+Enter` 接受
  - 可以作为开发环境打开文件夹等
  - 被收入[[editor-index]]
# 用例
- 选中`# 皮带 电蚊拍 洗牙器 自行车头盔`，`Ctrl + K`，翻译成英文，输出`# Belt, electric mosquito swatter, dental scaler, bicycle helmet`
# 注意
- 记得复制提示（避免intermittent服务器错误）
- 生成后可以
  - accept, reject
  - 手动删除手动修改，而不简单接受或拒绝
  - 在仍然有红绿高亮时，启动下一个任务（而不是完全接受或拒绝后再）
- 可以先写[[comment]]或部分代码，要求它补全
- 可以后台运作