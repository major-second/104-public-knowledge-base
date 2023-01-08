# 使用
## 快捷键
例如：
- [[editting]]的`Ctrl+C`（最常见）
- [[hotkeys]]的`C`
- shell中的`Ctrl+Shift+C`
  - 注意`Ctrl+C`是停止，这很坑。参考[[jupyter-notebook/basics]]
- [[mobaxterm]]中`shift+insert`
- [[built-in-keyboard-shortcuts/window]]中还有`Win + V`高级剪贴板！
## python
- [[standard-modules/copy]]
- 很多对象例如[[numpy/basics]]数组，[[tensor-calculator]]张量等都可以`.copy()`
- 表等等可以`[:]`
## 涉及公司内网
需要探索一下哪些地方，哪些方向可以复制粘贴等
为了合规，很有可能外网能贴进来，反过来不行
有些host互通，有些host不互通。自己探索公司的workspace软件！
# 优劣
- 好处
  - 两份相互独立，[[isolation]]，减少[[share-lock]]带来的[[python/trivial-mistakes]]等等
- 坏处
  - 重复内容，占用时间空间[[memory]]等