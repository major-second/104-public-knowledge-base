前置
- [[conda/installation]]

内容
- create: `conda create -n <env name> python=x.x`
    - 使用yaml文件创建：参考[[create-env-yaml]]
    - 区别于[[pip]]中的双等号`==`
- install packages: `conda install <name>`
  - `-c <名字>`指定channel，参考[[pytorch/basics/installation]]，有指定过`-c pytorch`或`-c pytorch-lts`
- enter an env: `conda activate <env name>`
- leave an env: `conda deactivate`
