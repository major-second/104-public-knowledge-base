- 普通使用
  - 一般直接`pip install 包名`
  - 根据前述讨论，当你在`conda`环境中，有可能需要`python3 -m pip install`
  - 有时（如[[gym/env]]，[[rllib/basics]]等）可能出现`包名[额外说明]`格式，例如`gym[atari]`
- 从源码安装python包（比如需要指定版本，比如conda和pip都找不到包时）
    - clone源码，进去
    - `pip install -e .`
      - 可用于[[create-python-package-for-pip]]后安装自己的
      - 当然，更一般的就是`pip install -e <相对或绝对路径>`
        - 这甚至被用在[[create-env-from-yaml]]中
    - 此时`pip list`可以看到有的包是在本地某个源码文件夹装的
    - 使用 [[toml]] 文件：[参考](https://stackoverflow.com/questions/62983756/what-is-pyproject-toml-file-for)
      - 和`requirements.txt`类似
- 批量安装依赖
  1. 原生方法：有个`requirements.txt`里面一行一行写需要什么包，该文件内容形如
      ```text
      gym==0.19
      termcolor
      ```
    - 然后`pip install -r requirements.txt`即可
    - 注：`requirements.txt`有时还能看到`git`开头的一些行，表示一些从[[github]]等源码安装的包
  2. 和conda结合：[[create-env-from-yaml]]中的`dependencies - pip`子树
    - 当然为了更加保险，`dependencies`子树中可以增加`python=版本`和`pip=版本`
- 一般来说`pip`效率不如`conda`，但有些`pip`有的包`conda`没有，有些包`pip`才有较新版本
  - 所以`pip`简单来说就是质量差，东西多
- 涉及内网，不能联网：常常`pip install filename.whl`这样