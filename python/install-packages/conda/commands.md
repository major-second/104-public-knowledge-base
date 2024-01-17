前置
- [[conda-installation]]

[参考](https://docs.conda.io/projects/conda/en/stable/commands/index.html)

内容
- create: `conda create -n <env name> python=x.x`
    - 使用yaml文件创建：参考[[create-env-from-yaml]]，是`conda env create -f <path_to_yaml_file>`
    - 区别于[[pip]]中的双等号`==`
    - `-p`指定全路径（安装后续东西的前缀），防止[[7-permissions]]不足
      - 和`-n`是互相替代，异或关系
- install packages: `conda install <name>`
  - `-c <名字>`指定channel，参考[[pytorch/basics/installation]]，那里有指定过`-c pytorch`或`-c pytorch-lts`
  - `-y`就是[[silent]]
  - 安装后的包源码在哪？如果你`anaconda3`安装地址是`~/anaconda3`，那么装的第三方包就`~/anaconda3/envs/<环境名>/lib/python<x.x版本>/site-packages/<第三方包名>`
- enter an env: `conda activate <env name>`
- leave an env: `conda deactivate`
- 已经装过的包列表：`conda list`，可以结合[[find-grep]]中`grep`使用
  - 举例：`conda list | grep torch`
- 清理[[general-programming/cache]]: `conda clean --all`