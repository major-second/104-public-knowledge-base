使用示例
```python
for key in ['split', 'annotations', 'data', 'train_vids', 'val_vids', 'train_data', 'val_data', 'load_image']:
    setattr(self, key, getattr(dset, key))
```
看起来，很爽吧，省得一大堆`a.c = b.c`
然而坏处是：搜索`self.split`可能有些引用找不着
总之元编程会提升新手错误率