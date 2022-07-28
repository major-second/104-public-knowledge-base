前置
- [[conda/installation]]

内容
- create: `conda create -n <env name> python=x.x`
    - 使用yaml文件创建：参考[[create-env-yaml]]，是`conda env create -f <path_to_yaml_file>`
    - 区别于[[pip]]中的双等号`==`
- install packages: `conda install <name>`
  - `-c <名字>`指定channel，参考[[pytorch/basics/installation]]，那里有指定过`-c pytorch`或`-c pytorch-lts`
  - `-y`就是[[silent]]
- enter an env: `conda activate <env name>`
- leave an env: `conda deactivate`
- 已经装过的包列表：`conda list`，可以结合[[find-grep]]中`grep`使用
  - 举例：`conda list | grep torch`
