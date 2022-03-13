注：mujoco原先收费，现在开源。200之前的版本需要激活key（但现在官方公开了免费的激活key了），之后的不需要
# 开源版本安装
- 下载安装MuJoCo到标准位置（参考[repo](https://gitcode.net/mirrors/openai/mujoco-py)）
  - 不用翻墙，是个镜像
> Download the MuJoCo version 2.1 binaries for Linux or OSX
> Extract the downloaded `mujoco210` directory into `~/.mujoco/mujoco210`
- 先看官网troubleshooting补包和`ln`一下
  - 否则一会编译缺东西
  - 其实缺啥就去百度谷歌看装啥能补就行
  - 这里比较坑的是它的troubleshooting列举不全。有个缺的要自己补（`apt install patchelf`他没写）
- 在`~/.bashrc`（或`~/.zshrc`，如果你用`zsh`）中，添加一些环境变量
  - 具体添加什么，一会`import mujoco_py`的时候会看到。他让你加啥你就加啥
  - 并`. ~/.bashrc`
- 交互验证安装（以下步骤来自[repo](https://gitcode.net/mirrors/openai/mujoco-py)）
  - （在这之前可能要先`conda activate <你的环境>`）
```shell
$ pip3 install -U 'mujoco-py<2.2,>=2.1'
$ python3
import mujoco_py
import os
mj_path = mujoco_py.utils.discover_mujoco()
xml_path = os.path.join(mj_path, 'model', 'humanoid.xml')
model = mujoco_py.load_model_from_path(xml_path)
sim = mujoco_py.MjSim(model)

print(sim.data.qpos)
# [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

sim.step()
print(sim.data.qpos)
# [-2.09531783e-19  2.72130735e-05  6.14480786e-22 -3.45474715e-06
#   7.42993721e-06 -1.40711141e-04 -3.04253586e-04 -2.07559344e-04
#   8.50646247e-05 -3.45474715e-06  7.42993721e-06 -1.40711141e-04
#  -3.04253586e-04 -2.07559344e-04 -8.50646247e-05  1.11317030e-04
#  -7.03465386e-05 -2.22862221e-05 -1.11317030e-04  7.03465386e-05
#  -2.22862221e-05]
```
# 老版本安装（需要激活key）
老版本用于跑老环境（比如`requirements.txt`指定了老版本的`mujoco_py`时）
- [下载](https://www.roboti.us/download.html)
  - 比如`200`版本
- 用`unzip`解压，并拷到`~/.mujoco/`（类比刚刚操作）
  - 注意文件夹要改名，比如把`linux`字样去掉
- [官网公布的key](https://www.roboti.us/license.html)拷到`~/.mujoco`
- 其它就类似了。直接`pip`安装或者用其他人写的`requirements`安装就都可以了
  - 当然，`pip`安装的版本也就不能是刚刚的`2.1`了
  - 当然，环境变量加的也不一样
  - 当然，验证安装的`python`代码也不一样
# issue
一个常见的github issue: 锁住，死循环
https://github.com/openai/mujoco-py/issues/424
解决方法：删除
`your-virtualenv/lib/python3.7/site-packages/mujoco_py/generated/mujocopy-buildlock.lock`