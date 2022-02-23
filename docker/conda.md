## 基础
静默安装：`-b`
但是这样不会自动`activate`和`init`
所以需要先`. ~/miniconda3/bin/activate`（当然，前面安装时你可以自己`-p`指定别的路径，那么这时路径就不同），使得可以**临时**使用`conda`指令，然后`conda init`，再使得以后可以永久使用
## docker的不同
上面的步骤在docker中想完成，必须要先[[docker-file]]中使用`SHELL ["/bin/bash", "-i", "-c"]`
原理是`conda init`其实是在`~/.bashrc`里加东西，而后者只有`-i`才会`source`到
### `RUN`之间相互独立造成麻烦
参考https://zhuanlan.zhihu.com/p/393326779
有趣的是，该篇不涉及`. ~/miniconda3/bin/activate`问题，因为它使用官方装好conda的镜像了