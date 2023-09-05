- 前置[[shell-type]]

`.sh`中使用`conda`和交互式不一样。需要先
```sh
CONDA_DIR="$(conda info --base)"
source "${CONDA_DIR}/etc/profile.d/conda.sh"
```
docker中的[[conda-in-docker]]，里面也有交互式和非交互式不一样的一些体现