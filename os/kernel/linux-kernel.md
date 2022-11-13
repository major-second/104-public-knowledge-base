[toc]
## basics
参考
http://zhaoxuhui.top/blog/2021/02/20/ubuntu-linux-kernel-installation.html
- 内核和硬件密切相关，比如实时内核，对机械臂非常有用。实时内核参考
https://blog.csdn.net/huangjunsheng123/article/details/116202848
和
https://github.com/ApolloAuto/apollo/blob/master/docs/howto/how_to_install_apollo_kernel_cn.md
如果需要实时内核，我们就需要先下载一般内核，解压打补丁，打包再安装
- 操作系统是内核态和用户态工具的总称，内核只是一部分
内核层和用户层是两个东西（比如重装内核肯定不影响你`~`里存的音乐和`git`库等）
- 拓展知识：同时在CPU Ring0上跑的只能有一个内核
所以得在启动的时候就决定好启动哪个（开机时，在[[grub-menu]]中可以选择！）
像Linux装多个内核就可以用不同的内核启动，但是用户态的东西都是共享的。一般多个内核，可以称为“同一个系统”
- 内核安装：本篇主要都是编译打包等等花时间。其实安装很快
  - 其实可以一次打包以后到处安装，很方便
## 下载内核（可能还有补丁）
去
www.kernel.org/pub/linux/kernel
里面找url并下载
- 注：有时可能要下载的除了内核，还有补丁
比如：安装实时内核，需要4个文件：内核`.xz`，内核`.sign`，补丁`.xz`，补丁`.sign`。
- 内核和补丁的版本号要对应，比如这里的4.14.12

示例：比如以下的4个`url`
https://www.kernel.org/pub/linux/kernel/v4.x/linux-4.14.12.tar.xz
https://www.kernel.org/pub/linux/kernel/v4.x/linux-4.14.12.tar.sign
https://www.kernel.org/pub/linux/kernel/projects/rt/4.14/older/patch-4.14.12-rt10.patch.xz
https://www.kernel.org/pub/linux/kernel/projects/rt/4.14/older/patch-4.14.12-rt10.patch.sign
无论用浏览器保存还是`wget`都行
- 为了保险起见我们可以用`uname -r`查看操作系统发行编号。`uname -a`显示更多信息
安装新内核和你原来用的版本接近，自然就更不容易出岔子
## 解压校验
解压可能有几层。这里有意思的是：先解压一层，校验，再解压一层。
`xz -d <第一个文件>.xz`
`xz -d <第二个文件>.patch.xz`
`-d`不保留源文件
校验：尝试`gpg --verify linux-4.14.12.tar.sign`（你的版本号可能不同）。
第一次运行时会报错缺少公钥。只需要`gpg --keyserver hkp://keys.gnupg.net --recv-keys 0x<复制得到的16进制串>`即可
- 注：如果在`keys.gnupg.net`找不到，那就改成`keyserver.ubuntu.com`，或者上网找别的可能的server

同样方法校验另一个文件
校验成功能看到`Good Signature`字样
然后再解压`.tar`（又一层！）
`tar -xf <文件名>.tar`
## 选做：打补丁
`cd <解压出的文件夹>`
`patch -p1 < ../<文件名>.patch`
## 选做：调整config
我们在已有config的基础上进行修改，避免出现问题
`cp -v /boot/config-$(uname -r) .config`
参考[[11-basic-scripting-partA]]中`$()`的含义
[[cp-mv-rm]]中`-v`的含义
在此基础上手动调整`.config`. 直接操作不太方便。不如使用一定的界面。比如
`sudo apt-get install build-essential libncurses-dev bison flex libssl-dev libelf-dev`
`make menuconfig`
- 在界面中上下左右和回车操作 to modify the configs. 非常方便
  - press `/` to search
- 例如实时内核就需要找到`General Step -> Preemption Model`，改成`Fully ...`使得实时性最强
- 例如有时`SYSTEM_TRUSTED_KEYS`字段造成麻烦，需要编辑（参见下一节）
- 保存退出等操作也都可用上下左右和回车操作
## 打包安装内核
### get `.deb`
`sudo make -j4 deb-pkg`
注：`make`的`-j4`表示并行（更快）。但其可能让报错不容易找。比如刚刚说的`SYSTEM_TRUSTED_KEYS`造成的问题，就可能被埋起来。有利有弊
ref: [[make]]
### troubleshooting
- `BTF`相关，[reference](https://stackoverflow.com/questions/61657707/btf-tmp-vmlinux-btf-pahole-pahole-is-not-available)
```text
  │ Symbol: DEBUG_INFO_BTF [=n]                                                                                                                                                         │  
  │ Type  : bool                                                                                                                                                                        │  
  │ Prompt: Generate BTF typeinfo                                                                                                                                                       │  
  │   Location:                                                                                                                                                                         │  
  │     -> Kernel hacking                                                                                                                                                               │  
  │       -> Compile-time checks and compiler options                                                                                                                                   │  
  │ (1)     -> Compile the kernel with debug info (DEBUG_INFO [=y]) 
```
change to `n`
i.d. `[*]` -> press `n` key -> `[ ]`
- `TRUSTED_KEYS`相关
[参考](https://wiki.gentoo.org/wiki/Signed_kernel_module_support)
简单的办法就是搜索`SYSTEM_TRUSTED_KEYS`，定位到该字段，去除其内容
```text
  │ Symbol: SYSTEM_TRUSTED_KEYS [=]                                                                                                                                                     │  
  │ Type  : string                                                                                                                                                                      │  
  │ Prompt: Additional X.509 keys for default system keyring                                                                                                                            │  
  │   Location:                                                                                                                                                                         │  
  │     -> Cryptographic API (CRYPTO [=y])                                                                                                                                              │  
  │       -> Certificates for signature checking                                                                                                                                        │  
  │ (5)     -> Provide system-wide ring of trusted keys (SYSTEM_TRUSTED_KEYRING [=y])  
```
remove it

After modifying those configs, run `sudo make -j4 deb-pkg` again.
### install `.deb`
打包完成之后，`..`中有一些`.deb`
现在直接
`sudo dpkg -i ../<文件名>.deb <后面还有3个>`（所有`.deb`都要写上）
- 关于实时内核
重启，`uname -a`可以看到`PREEMPT_RT`字符串（注意如果是[[multiple-ubuntu-versions]]，则需要旧系统手动用`sudo update-grub`更新[[grub-cfg]]）
`cat /sys/kernel/realtime`内容为`1`
这时，`nvidia-smi`用不了了，直接参考[[rt-kernel-gpu]]即可