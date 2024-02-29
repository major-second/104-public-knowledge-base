# general
- 前置
  - [[slack]]
- 安装：`<name>.slack.com/apps`下属url
  - 注意选择[[slack-workspaces]]
- general用法
  - 可以在app 的 pane选择相应图标直接对话
  - 可以 `@`进channel参与。例如[[slack-extensions#chatgpt]]
- [参考](https://silenceallat.top/save_html/%E5%B0%91%E6%95%B0%E6%B4%BE/file/Slack%20%E4%B8%AD%E6%9C%89%E5%93%AA%E4%BA%9B%E5%80%BC%E5%BE%97%E6%8E%A8%E8%8D%90%E7%9A%84%20Bot%20-%20%E5%B0%91%E6%95%B0%E6%B4%BE.html)
# [[tools/zoom]]
- `/zoom`等命令，聊天框中创建会议，加入等等
# [[google-calendar]]
- `/gcal`命令 [[CLI]]
  - `/gcal today`看今天，等
- 但也有[[GUI]]可以设置event，邀请别人，发邮件等
# standups
- [[standuply]]
  - 设置report名字后，`/run name`可以跑，并在slack收结果
  - `/standup [@user1 @user2] [#channel]` 相当于快速问卷
    - 比如使用例子：`关一下服务器行不行`
- [[sup]]
  - 免费版可用人数更多，推荐！
# [[git]]
- [[github]]
  - 使用extension, connect（可能需要浏览器登录github认证得到验证码），然后可以`/github subscribe`之类的命令
- [[gitlab]]
  - 参考[[gitlab]]
# [[integration-webhook]]
- legacy / will be deprecated
- 被gitlab slack apps替代
  - 但是对于内网的gitlab还是没法替代hhh
- 名称：Incoming webhooks
  - 步骤
    - 搜索这个名字的app
    - 选择[[slack/slack#范围]]（如channel）
    - 给出[[integration-webhook]]
    - 然后复制给[[gitlab]]等地方
      - 例如[[gitlab]]可以用，设置中有integration版块，可以复制hook过来
  - 结果：这样[[push-pull#push]]（或者其他你设置的动作）时会自动通知
# [[chatgpt]]
- 搜索`gpt`，有个名字叫`Q`的就是集成在 slack中的 chatgpt
- 可以 `@`它问问题，thread中回复，转发内容等，很方便
- 240228 [[pricing]]有官方后门，他直接提示你 `Need more time? Re-install for +14 days.`，然后你就可以再用14天，可以看成他想提升市占率
# 其他
- [[cloud-storage]]
  - [[dropbox]]（自动preview，方便分享等）
  - [[google-drive]]
- `latexbot`: [[latex]]
  - command: `/latex`