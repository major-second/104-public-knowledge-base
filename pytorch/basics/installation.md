前置
- [[conda-installation]]或[[pip]]
  - 最好[[conda/commands]]首先创建全新`conda`环境，否则可能影响[[dependencies]]求解
- 如果需要GPU，则需要[[ubuntu-nvidia-drivers]]，并务必提前了解[[torch-cuda]]防止兼容性出问题
- 如果懒得自己安装，可以用在线的，[比如微软提供的](https://docs.microsoft.com/en-us/learn/modules/intro-machine-learning-pytorch/)

步骤
- 上[官网](https://pytorch.org/get-started/locally/)查conda或pip命令
  - 比如`conda install pytorch torchvision torchaudio cudatoolkit=10.2 -c pytorch-lts`即可
  - 其中`lts`意思是长期支持，参考[[version]]
  - 如果`pytorch-lts`这个channel太慢，可以考虑改为`-c pytorch`，也参考[官网](https://pytorch.org/get-started/locally/)
  - 或`conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/`后，直接`conda install pytorch torchvision torchaudio cudatoolkit=10.2`，而不用`-c`指定的channel
    - 当然，不用官方channel，其它的channel有可能缺你想要的版本，甚至默认给你装cpu版本的，参考[[channel]]
  - 当然，如果你要装其它版本，也相应在[官网locally](https://pytorch.org/get-started/locally/)和[官网previous-versions](https://pytorch.org/get-started/previous-versions/)里查询
- `torchaudio`，`torchvision`是附属，不是必要的（不过也推荐顺便装上）