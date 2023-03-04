# 概述
- 一般人认为计算机一就是一，二就是二具有确定性
- 但有时会有不确定性。有时有用，有时有麻烦
# 现象
- 多次训练神经网络，种子不同，效果不一致
- [[pickle/basics]]存下来同一个对象，[[xxd-diff]]时告诉你两者不同。例如[[misc/equality]]
- 例如网络条件随机导致[[ros/installation]]中`rosdep update`每次可能成功一部分，没法一次成功，通过几次尝试覆盖全部update需求
# 引入和利用
- 例如[[rand]]中提到的在C++中如何引入随机性，并利用它防止你的哈希被hack
- 例如python的`random`和`np.random`等
  - [[parallelism]]中提了一嘴用`numpy`生成随机数
- 例如深度学习防止[[overfit]]的[[dataloader]] shuffle，随机dropout等
- 例如随机运行很多种子挑最好的结果（这样别太过分）
# 防止负面影响
目的：比如[[general-principles/debug]]对拍用等
## 去除随机性
- 例如gym的[[seed]]设置，`<env>.seed(42)`
- numpy的`np.random.seed(42)`
- 原生`random`的`random.seed(42)`
- [[sklearn]]的`model.random_state = state`
## 跑多几个取平均
- 理论基础参考[[prob/LLN]]
- 比如涉及神经网络等训练，跑多个随机种子取平均值，稳定地看结果
  - 这时常见所需的操作和技能（请参考）
    - 对于[[tensorboard]]的[[lightning/logs]]文件夹的分开设定
      - 不管你是调[[lightning/basics]]这种包还是自己存[[tensorboard]]，都有办法让[[lightning/logs]]文件夹分开
    - [[command-line-arguments/basics]]传命令行参数
    - [[isolation]]思想，例如[[torch-cuda]]指定用卡