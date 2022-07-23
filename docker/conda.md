## 基础
conda的静默[[silent]]安装所需参数：`-b`
但是这样不会自动`activate`和`init`
所以需要
- 先`. ~/miniconda3/bin/activate`
  - 当然，前面安装conda时你可以自己`-p`指定别的路径，那么这时路径就不同
  - 使得可以**临时**使用`conda`指令
- 然后`conda init`
  - 实质即添加一部分脚本到`~/.bashrc`等`rc`文件
  - 如果是[[zsh]]当然就添加到`~/.zshrc`
  - 使得以后可以永久使用

这是[[temp-solution]]的思想
## docker的不同
### 指定`-i`
上面的步骤想在docker中起作用，一种方法是[[docker-file]]中使用`SHELL ["/bin/bash", "-i", "-c"]`，指定用`-i`选项的bash
原理：
- `conda init`其实是在`~/.bashrc`里加东西
- 而这些加的东西只有`-i`时才会`source`（被执行）到
### 直接加`PATH`
[参考](https://stackoverflow.com/questions/69259311/why-do-i-got-conda-command-not-found-when-building-a-docker-while-in-base-im)
加`PATH`也能解决这一问题
宿主一般不加，防止搞乱环境
docker容器中可以加
### `RUN`之间相互独立造成麻烦
参考https://zhuanlan.zhihu.com/p/393326779
原因是每个`RUN`都是独立的layer
注：该篇不涉及`. ~/miniconda3/bin/activate`问题，因为它使用官方装好conda的镜像了。这是另一个问题