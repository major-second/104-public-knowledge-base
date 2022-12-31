[toc]
# 总述
- 俗话说得好，重启，重装，重买
- 上面一句话看出：显然refreshing有不同等级
  - 有时我们需要了解精确到哪一等级就行了，以节省时间精力
    - 比如[[nbextension]]中的：能重新打开窗口就不需要restart整个笔记本
## 重启
- [[zsh]]中设置默认shell为`zsh`需要**重新登录**
- [[special-files]]提到
  - `git rm --cache`命令停止track某些**已经被track的**文件
  - 并更新`.gitignore`，使得**接下来它们被忽略**
    - 更进一步，如果在用vscode，则可能需要**重启**vscode才能让vscode识别此事实
  - 只重启终端不重启vscode还没用
- [[jupyter-notebook/basics]]中提到的用`Restart`内核使得`.py`文件的改动生效
- 和[[quit]]当然有联系（[[quit]]往往是彻底干净重启所需要的）
  - 例如任务管理器[[quit]] Apps/Background Processes/Windows Processes
  - 依次要更加慎重
## 重装（可能也要重启）
- [[assets]]中vulkan相关错误在**重装**vulkan sdk后需要**重启**
- [[timeshift]]和[[tmux]]的互动可能把tmux弄崩，**重装**tmux并**重启**即可
- 打开游戏时`d3dx9_42.dll`出错？**重装**DX即可
- [[torch-cuda]]中提到有时[[conda/commands]]和[[pip]]**卸载**已有的[[pytorch/basics/installation]]就能**重装**成功GPU版本的`torch`
## 更新文件
- [[dot-ssh]]中的**重新创建文件夹**
- [[software-management/source]]中处理`Conflicting values set for option Signed-By regarding source ...`的方法：删掉并**重新写文件**
- 及时**删除**[[general-principles/cache]]并**重新生成**，防止接下来使用错误的缓存文件
- 清理[[cookies]]
## 硬件层面
- [[interface]]提到的重新插拔接口
  - 比如[[wired-connection]]
  - 比如[[franka-panda/troubleshooting]]
- 例如[某款耳机控制键用不了的问题](https://helpguide.sony.net/mdr/wi1000x/v1/zh-cn/contents/TP0001514117.html)
- 手机[[android/battery]]不耐用了直接换电池
## 覆盖
有时直接“刷新”不够彻底，或做不了，则需要覆盖
- 比如清空回收站可能还能找回，但重新写入就会彻底把文件覆盖
- 比如[[settings/keyboard-shortcuts]]中`Ctrl+P`覆盖（打断）其它的“上方跳出界面”
## 其它
- [[settings-and-configurations]]设置东西之后要**更新**。包括但不限于
  - `source` [[shrc]]
    - `. ~/.bashrc`，[[zsh]]中的`. ~/.zshrc`等等
    - 当然[[6-env]]中所说**重开终端**相当于`. ~/.bashrc`了，可以作更新
  - [[configure]]中提到的powershell需要新开进程才能用上新的代理设置
    - `Start-Process powershell.exe -NoNewWindow -Wait -ArgumentList <路径>`
  - [[yama-ptrace-scope]]中的`sudo sysctl -p /etc/sysctl.d/10-ptrace.conf`
  - [[software-management/source]]的`sudo apt update`
- 连接学校/公司内网等需要登录的，如果登录界面出问题，尝试手机wi-fi设置中forget这个网络，然后再连接
- 做事没有有头有尾（[[finally]]处搞出来的锅）往往都要“重置”解决
- python导入东西的重置：参考[[import/basics]]
- [[node]]中提到的geph，改变是否监听等需要断开重连
# 副作用
有时，要求稳定，不能更新
- 比如[[tensorboard]]的`logdir`如果删除重建了，你就不得不重新启动`tensorboard`命令