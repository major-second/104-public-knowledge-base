- [[package-managers]]
- `pip`本身来源：
  - windows
    - [[windows-python]]可选同时带上pip
    - 之后有可能出现`pip`不行但`python -m pip`可以
  - linux
    - `python2`：`apt install python-pip`
      - `pip --version`一下看到版本和所在位置（看到`python2.7`字样）
    - `python3`：`apt install python3-pip`
        - 此时`pip3 --version`查看版本
        - `pip --version`一下，发现这个在`/usr/lib/python3`而不在`python2.7`
          - 这和`apt install python-pip`后现象完全不同
        - `pip3 install --upgrade pip`做[[general-software-technical/upgrade]]
    - 关于`python3 -m pip`和`pip3`区别，[参考](https://stackoverflow.com/questions/41307101/difference-between-pip3-and-python3-m-pip)
      - 产生该现象的原因：可能是本地`python`版本比`conda`虚拟环境版本低
        - 此时，本地`pip`能为虚拟环境装包，但可能缺包！
        - 例如`python3.6`无法装`pip22`从而无法装`tensorflow2.9`
          - 即使`pip3 install --upgrade pip`也不行
        - 需要`python3 -m pip`
      - 举例：
```sh
(<conda环境>) <用户>@<服务器名>:~/<路径>$ which pip
/home/<用户>/.local/bin/pip
(<conda环境>) <用户>@<服务器名>:~/<路径>$ which python3
/home/<用户>/anaconda3/envs/<conda环境>/bin/python3
(<conda环境>) <用户>@<服务器名>:~/<路径>$ python -m pip --version; pip --version
pip 22.2.1 from /home/<用户>/anaconda3/envs/<conda环境>/lib/python3.7/site-packages/pip (python 3.7)
pip 21.3.1 from /home/<用户>/.local/lib/python3.6/site-packages/pip (python 3.6)
```
- [[settings-and-configurations]]
  - 要不然直接编辑文件
  - 要不然使用`pip config`命令（需要较新[[version]]）
  - 比如`pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple`使用清华源（不翻墙时更快）
  - 比如`pip config set global.index-url https://mirrors.ustc.edu.cn/pypi/web/simple`使用科大源
  - 但是清华、中科大等源可能缺东西。可以`-i https://pypi.python.org/simple/`使用`pypi`源
    - 只要下载一次[[general-principles/cache]]了，以后就可以在本地用
- `sudo rm -r ~/.cache/pip`清除[[general-principles/cache]]
- 使用: [[pip-install]]