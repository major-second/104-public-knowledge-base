前置：
- [[conda/installation]]或[[pip]]
- 如果需要GPU，则需要[[ubuntu-nvidia-drivers]]
  - 或者使用在线的，[比如微软提供的](https://docs.microsoft.com/en-us/learn/modules/intro-machine-learning-pytorch/)

步骤：
- 上[官网](https://pytorch.org/get-started/locally/)查conda或pip命令
  - 比如`conda install pytorch torchvision torchaudio cudatoolkit=10.2 -c pytorch-lts`即可
  - 其中`lts`意思是长期支持，参考[[version]]
  - 如果`pytorch-lts`这个channel太慢，可以考虑改为`-c pytorch`，也参考[官网](https://pytorch.org/get-started/locally/)
  - 或`conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/`后，直接`conda install pytorch torchvision torchaudio cudatoolkit=10.2`，而不用`-c`指定的channel
- 此处不用前置CUDA
  - 原因：看[官网](https://pytorch.org/get-started/locally/)，`conda`和`pip`都有直接可装的`cudatoolkit`，这就包含了CUDA
- `torchaudio`，`torchvision`是附属，不是必要的（不过也推荐顺便装上）
