做好备份（最好还是多平台冗余备份），定期更新备份，最大程度减少[[hardware]]坏，系统坏等的损失
- 比如
  - 文件的备份（改之前先复制一份）
  - [[git-installation]]版本管理
    - [[commit]]方便本地[[reset]]
    - [[push-pull]]方便多平台容灾
  - 整机备份（[[timeshift]]，虚拟机，docker等）
  - [[wechat-tips]]中聊天记录备份
  - [[keybase]]也可多平台备份一些小文件、文本记录等
- 导致过“回档”的情况
  - apt重装，`autoremove`，把有用的东西删了太多（甚至`pip`都没了），不知道怎么弄回来
  - [[ubuntu-nvidia-drivers]]装了黑屏