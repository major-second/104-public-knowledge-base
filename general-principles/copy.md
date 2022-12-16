# 使用
## 快捷键
例如：
- [[editting]]的`Ctrl+C`（最常见）
- [[hotkeys]]的`C`
- shell中的`Ctrl+Shift+C`（注意`Ctrl+C`是停止，这很坑。参考[[jupyter-notebook/basics]]）
## python
- [[standard-modules/copy]]
- 很多对象例如[[numpy/basics]]数组，[[tensor-calculator]]张量等都可以`.copy()`
- 表等等可以`[:]`
# 优劣
- 好处
  - 两份相互独立，[[isolation]]，减少[[share-lock]]带来的[[python/trivial-mistakes]]等等
- 坏处
  - 重复内容，占用时间空间