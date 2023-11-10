[toc]
# 前置和参考
- [[CRUD]]
- [[dont-trust-others]]
- [[pricing]], [[general-principles/account]], [[open-source]]
- [[memory]], [[resource-management/disk]]
# 安装
## [[CLI]]
- [[package-managers]]
  - [[apt]]
    - [[software-management/source]]
  - [[pip]]
  - [[conda]]
  - [[conan]]
## 下载安装包/程序安装
- 安装包可能需要访问网络再下载东西也可能不要（“离线包”）
  - [[windows-cpp-compilers#mingw-w64]]就提到离线[[workaround]]
- 参考
  - [[download-resource]]
  - [[file-format]]
    - [[binary-executable]]
    - [[zip-unzip]]
      - [[linux-zip-unzip]]
- win的`exe, msi`, linux的`sh, deb`, 安卓`apk, xapk`等
- [[install-from-sh]]
## 绿色软件
- 无需安装，可以移动不[[dependencies]] on 路径
- [[sumatrapdf]]
### Standalone, SA
- 有时需要[[windows/env-var]]等等修改
- 一般步骤
  - 直接下载 SA 程序（比如`.exe`），放到指定路径
    - 可以网页点击下载或者[[curl-wget]]
  - 增加[[windows/env-var]]等
- 例子
  - [[rcc]]
  - [[robo]]
## 应用商店
- 官方或非官方
- [[apple-app]]
- [[huawei-google]]
## [[build-from-source]]
[[github]], [[other-hubs]]
## 系统内置
自己设置之类地方探索探索就有
# 查询
- 更新，版本管理
  - [[version]], [[dependencies]]
# 删除
- 以及管理开机自启[[startup]]，互相唤醒，后台等
- [[disk]], [[memory]]
- [[quit]], [[aida64]]
- [[optimize]]