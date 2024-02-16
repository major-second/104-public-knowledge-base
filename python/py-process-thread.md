# 伪多线程
- https://zhuanlan.zhihu.com/p/114453309
- py多线程并不真正
  - GIL 全局解释器锁 [[share-lock]]
  - cpu密集无优势
  - [[i-o]]密集有优势
- 联系[[async-await]], [[coroutine]]，只不过线程是系统级