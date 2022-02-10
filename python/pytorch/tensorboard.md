tensorboard本来是用于tensorflow的可视化，但也可以用于pytorch
[官方教程](https://pytorch.org/tutorials/recipes/recipes/tensorboard_with_pytorch.html)
- 之后另开一个终端，`tensorboard --logdir <目录> --port <端口>`
  - 注：如果要远程看，需要`--bind-all`参数
- 然后远程看：浏览器输入`<ip>:<端口>`