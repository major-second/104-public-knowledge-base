自己做定制和优化固然好，但是时刻要留心眼。是不是可能就是它出锅？毕竟其他人可能只考虑了标准情况，没有考虑全部情况
- 比如用[[zsh]]
  - 对于中括号`[]`就会出问题
  - 在[[dev-env]]中也会带来错误
  - 对`echo "\\n"`的输出结果也和[[11-basic-scripting-partA]]讲的不同
  - 对`sudo apt remove *nvidia*`的结果也不同
  - [[franka-ros-interface]]只能用`bash`
- 比如[[proxy/usage]]讲到有些地方开了代理就上不了
- 比如[[nbextension]]可能导致[[jupyter-notebook/tqdm]]中`tqdm_notebook`用不了（不兼容）
- 比如不常用的conda [[channel]]可能缺少最新版本