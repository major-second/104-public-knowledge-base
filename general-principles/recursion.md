# 理论
todo
# 算法题中的[[oi-wiki-basic/recursion]]
- 例如[[10-regular-expression-matching]]
# 一般程序中的递归（提升可读性）
- 例如`torch`把复合对象递归地找到其中所有的`Tensor`并移至指定GPU（参考[[device]]）
- 路径`lib\python3.7\site-packages\torch\nn\parallel\distributed.py`
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
# 无限循环和自相似
- 递归没有出口/没考虑好情况可能导致无限递归循环，出现TLE等
- 但数学中往往可以“自相似”，例如$x = 1-x$，并不会无限循环，而可以解出$x$
  - 例如[[introduction]]中，“第一次丢出硬币正面需要多少次投掷”
  - 例如[[5-markov-chain]]中，“达到某吸收态的概率”