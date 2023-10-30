- [官方文档](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.view.html)
- 前置
  - [[encode-decode#计算机编码]]
  - [[general-copy]] vs. [[share-lock]]
  - [[contiguous]]
- 共享同一块内存而非[[numpy-basics#Copying Arrays]]
- 用处
  - 改变bit per element，这需要很了解[[encode-decode#计算机编码]]
  - ```python
    print(np.array(['1'] * 8).view('U4'))
    print(np.array([1] * 8).astype(np.uint8).view(np.uint16))
    ```