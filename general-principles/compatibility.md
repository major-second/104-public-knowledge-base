# forward
- [参考](https://zhuanlan.zhihu.com/p/28195702)
- 向前兼容（Forward Compatibility）
  - 指老的版本的软／硬件可以使用新版本的软／硬件产生的数据
  - “Forward”一词在这里有“未来”的意思，“向前”就是“向未来”，现在的软件可以用未来的数据
  - 很多时候汉语中这个“向前”是指“从前”还是“之后”是有歧义的
- 例子
  - 比特币区块链系统是向前兼容的，老版本的节点依然可以验证新版本产生的区块，这也是比特币区块链不会产生永久分叉的基础
# backward
- 向后兼容（Backward Compatibility）和 [forward](#forward)相反
- Windows操作系统是向后兼容的，大部分针对Windows 7开发的软件依然可以很好的运行在Windows 10下。Windows通过保证系统API的稳定不变，只增加不删除的策略，保证了老系统上开发的软件可以很容易的在新系统上运行
# 自己开发时
- 开发时重构想保证 [backward](#backward)
  - 可以保留一些旧接口，标记`deprecated`
  - 比如本来`0到1到2`，你现在可以
  - `0到1'`，`1'到1`，`1'也到2`
  - 这样原来的1也能有，但我们主workflow是`0到1'到2`
  - `1`就是deprecated