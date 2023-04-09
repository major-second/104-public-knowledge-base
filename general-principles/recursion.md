# 理论
- 参考
  - [[self-similarity]]
  - [[induction]]
  - [[dp]]
# 算法题中[[oi-wiki-basic/recursion]]
- 例如[[10-regular-expression-matching]]
# 互相递归调用
- [[q-v]]
  - 防止互相递归不好计算：[[q-learning]]
# 一般程序中
## 命令行
- 有些自动递归（这时要防止递归运行太多太慢）
  - [[cp-mv-rm]]中`mv`自动递归
  - `du`加`-s`才不递归
  - [[ls-tree]]中`tree`加`-L 数字`才不递归
- 有些不自动递归
  - [[ls-tree]]中`ls`加`-R`才递归
  - `chmod`加`-R`才递归 ([[7-permissions]])
  - [[cp-mv-rm]]中`cp, rm`加`-r`才递归
## 自己写
- 可提升[[readability]]
- 例如`torch`把复合对象递归地找到其中所有的`Tensor`并移至指定GPU（参考[[device]]）
  - 路径`<path\to>\lib\python3.7\site-packages\torch\nn\parallel\distributed.py`
  - 版本`'1.9.0+cu102'`
```python
def to_map(obj):
    if isinstance(obj, torch.Tensor):
        if obj.device == torch.device("cuda", target_gpu):
            return (obj,)
        if not self.use_side_stream_for_tensor_copies:
            return (obj.to(target_gpu),)
        else:
            # Perform CPU -> GPU copies in a background stream. This code is
            # motivated from similar logic in torch/nn/parallel/_functions.py
            stream = _get_stream(target_gpu)
            with torch.cuda.stream(stream):
                output = obj.to(target_gpu)
            # synchronize with the copy stream
            with torch.cuda.device(target_gpu):
                current_stream = torch.cuda.current_stream()
                # Sync the current stream with the copy stream
                current_stream.wait_stream(stream)
                # Ensure tensor memory is not reused until work on
                # main stream is complete
                output.record_stream(current_stream)
            return (output,)
    if is_namedtuple(obj):
        return [type(obj)(*args) for args in zip(*map(to_map, obj))]
    if isinstance(obj, tuple) and len(obj) > 0:
        return list(zip(*map(to_map, obj)))
    if isinstance(obj, list) and len(obj) > 0:
        return [list(i) for i in zip(*map(to_map, obj))]
    if isinstance(obj, dict) and len(obj) > 0:
        return [type(obj)(i) for i in zip(*map(to_map, obj.items()))]
    return [obj]
```
# 无限循环
- 递归没有出口/没考虑好情况可能导致无限递归循环，出现TLE等
- [[bootstrap]]中如果找不到[[workaround]]就可能出现鸡生蛋蛋生鸡无限循环
  - 所以很多时候第一个代理[[proxy-basics]]客户端这种“突破口”很重要
- 但数学中往往可以“自相似”[[self-similarity]]，例如$x = 1-x$，并不会无限循环，而可以解出$x$