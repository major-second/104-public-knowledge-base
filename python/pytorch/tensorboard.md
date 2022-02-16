tensorboard本来是用于tensorflow的可视化，但也可以用于pytorch
[官方教程](https://pytorch.org/tutorials/recipes/recipes/tensorboard_with_pytorch.html)
- 完成以上之后，另开一个终端
  - 到有`eventtf`那些文件的目录
  - `tensorboard --logdir . --port <端口>`
  - 注：如果要远程看，需要`--bind_all`参数（注意是下划线不是横杠）
- 然后远程看：浏览器输入`<ip>:<端口>`
  - 注：在（云服务器）宿主`B`使用`ssh -L`连接docker容器`C`，把`C`中端口转发到宿主`B`时，本地`A`一般不能直接通过`<宿主Bip>:<端口>`访问`C`的端口。这和docker配置有关
  - 但是可以`A`直接[[ssh连接docker容器]]`C`并使用`ssh -L`转发
- 用完即时清空文件，并停下`tensorboard`命令，免得下次用造成混乱
- issue: 如果装了多个版本可能报错duplicate啥的，参考[这个](https://stackoverflow.com/questions/57228487/valueerror-duplicate-plugins-for-name-projector)解决