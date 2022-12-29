# 概述
- [参考维基](https://zh.wikipedia.org/wiki/%E5%A2%9E%E5%88%AA%E6%9F%A5%E6%94%B9)
  - 增删查改，增删改查，C (Create) R (Read) U (Update) D (Delete)，最常见操作
  - 只会增删查改被称为CRUD boy，哈哈哈
- 各种[[settings-and-configurations]]，各种新软件新数据结构，第一件事往往就是学会CRUD
- 一般原则
  - 删除再增加等同于修改，所以可以只会三个
  - 有时增也是修改
  - “查”可能需要[[search-info/general]]技巧！
# 举例
- [[subsystem-for-linux]]：`wsl --install -d <distro>`，`wsl --unregister Ubuntu-20.04`，`wsl --list`等
- [[6-env]]：`export, unset, echo`
- [[conda/commands]]环境：
  - `conda create -n <env name> python=x.x`或`conda env create -f <path_to_yaml_file>`
    - 当然，实际使用还要`conda activate <env name>`
  - `conda deactivate; conda env remove -n <env name>`
  - `conda env list`
- [[config]]：`git config key.subkey value`，`git config --list`，`git config --unset key.subkey`
- [[systemd]]：`systemctl list-unit-files --type=service`，`sudo systemctl <start/stop/enable/disable/restart> ...`