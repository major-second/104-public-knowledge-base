- 好处：加密保护数据
- 坏处：
  - 让你的数据全部被加密丢失
  - 让[[dual-boot/steps]]时容易出现[[文件系统损坏]]需要[[fsck]]
- 反正：只有
  - 特别希望加密
  - 且不用[[dual-boot/steps]]
  - 且你能保护好recover key时
  - 才可以用bitlocker，否则就关掉！
- 平时自己关：开始菜单搜索bitlocker很容易看到

必看教程
- https://www.bilibili.com/video/BV1uP4y1s7e9/
- https://www.bilibili.com/read/cv12791018
- https://answers.microsoft.com/zh-hans/windows/forum/all/win10%E6%9B%B4%E6%96%B0%E5%90%8E%E8%87%AA%E5%8A%A8/8a89f904-9ba9-442b-ad5d-dc75f84b5356
- https://answers.microsoft.com/zh-hans/surface/forum/all/bitlocker/fa34b783-af98-441a-b751-0bea13ffeb42
- https://appuals.com/bitlocker-recovery-key-not-found/

已知issue
- 若很久没登录onedrive，则账号可能被冻结（“无法显示URL”）。登录onedrive解冻即可
- 手机和邮箱登录账号是不同的。可以都试试

办法
- 开机狂按f2还是可能能进bios
  - 如果是装双系统[[dual-boot/steps]]关了secure boot，那把secure boot重新打开是可以救回来的
- 你回忆一下第一次用电脑是不是用的本地账户而没有用微软账户，并且一路下一步没有关注bitlocker的事情。如果是，那基本上凉凉
- 其它的自己在网页看