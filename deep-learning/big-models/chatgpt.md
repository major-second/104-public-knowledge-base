- 前置
  - [[general-principles/account]]
  - 挂合适地区代理[[proxy/basics]]
     - 对地区可能有要求。如香港可能不行
  - 用虚拟手机号[[sms]]
  - 上 https://chat.openai.com/chat 注册即可使用
# 用法
- 在下方框敲东西让它回答
  - 可使用中文/英文/各种文字
  - 当然英文效果好
- 可以编辑之前的提问，或重试等
- 回答不完整，可以说`continue`或`继续`
- 某版本更新后，可以
  - 储存查看之前的chat内容
  - 自动生成摘要标题
# 提示工程
- 可以循序渐进给出指示
- 如果它不满足要求/预期，可以
  - 尝试Try again
  - 编辑输入，手动指出要求，重新submit
- 简单举例：
  - ![](prompt-example-0.png) 可以看到循序渐进
  - ![](prompt-example-1.png) 可以看到手动指出要求
# 记忆
- Thread中前面的信息会被记住
  - 左边可以清空Thread使得刷新记忆
- 具体的记忆信息例子
  - 应用：改文书，缩减文章等
  - 首先Here is a personal statement, please commit it to your memory as (A)，然后写一大段
    - 然后Here's another one. Please commit it to your memory as (B)然后写一大段
    - 然后例如问：
    - ![](prompt-example-memory.png)
  - 进阶：如果全文太长，可以一小段记为(A)，再一段记为(B)，等等，之后例如：
    - ![](prompt-example-memory-by-parts.png)
# 其它
- 可以发挥想象力，玩各种各样的事，如
  - 如何解决台湾问题
  - 普京给特朗普的情书
  - 针对博士后生活改编波希米亚狂想曲
  - 扛200斤麦子走……里需要做多少功？
  - （你懒得查文档时）帮助编程： ![](programming-aid.png)
    - 这里问到了[[matplotlib/basics]]中的`legend`位置
    - 有时会生成错误过时答案。所以用它写程序要小心
      - 但你可以把报错反馈回去，他可能就改正了
      - ![](correct-mistake.png)
  - 给出“指令”：`rephrase:`, `proofread:`, `expand:`之类的，后跟一段。可以降重、自动写文章等
  - ……
# 绕过限制
- 他有时会自我设限，但其实可以做。你可以想办法绕过
- 比如Please memorize不行，但Please commit it to your memory可能就行了