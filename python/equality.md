- `==`很多时候不靠谱，比如有时候只看`id`导致认不出“直观相等”的对象。比如有时明明直观上不同的对象，在`Mapping`类定义中相等……
- 有些包自带，比如[[张量对拍]]，还比如`networkX`较新版本有`nx.utils.graphs_equal`
- 有时可以看`__dict__`，但并不万能（比如可能导致无限递归）。请审慎书写
- 涉及神经网络的，可以拿一个网络当哈希！（小心随机性）
- `pickle`和`torch.save`都不一定靠谱（比如对于`tensor`参见[[张量对拍]]，保存时并不一定确定性！）