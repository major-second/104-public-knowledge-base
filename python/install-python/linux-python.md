- 有些版本系统自带python 2（`python`命令）
- python 3安装方法参考[[pip]]
  - `apt install python3-pip`
  - [[general-software-technical/upgrade]]? 可能需要 [[package-managers-source]]增加新的
- 如果只有`python3`命令没有`python`命令
  - 法一：有了[[anaconda]]，则可`conda activate base`之后，`python`就是[[anaconda]]环境中的`python3`
  - 法二：[[apt-install]]一下`python-is-python3`
  - 法三：手动[[ln-s]]