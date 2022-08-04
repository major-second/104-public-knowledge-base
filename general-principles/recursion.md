# 递归
## 理论
todo
## 应用举例
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