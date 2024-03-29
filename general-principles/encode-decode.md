- 编码解码

[toc]
# 计算机编码
- 总体原则
  - 二进制，[[7-the-power-of-2]]
  - 尽量统一
    - [[unicode]]
    - [[timestamps]]
- 如何编码
  - [[file-format]]
  - 整数
    - 参考[[overflow]]
    - unsigned问题
      - [[numpy-basics]]中有提到
      - [[pil-open-convert-save]]需要
  - [[float]]
  - 文字
    - [[ascii]]
    - [[encoding]]
    - [[unicode]]
  - 图片
    - [[pil-open-convert-save]]中图片和[[numpy-basics]]数组关系
## 时间戳
- [转换器](https://tool.lu/timestamp/)
- 例如2022.12，是1671693346秒（十位数）
- 那么其它时间戳可能单位不同。例如1649898030311019364（19位数）显然是纳秒
- `python`中`from time import time, time_ns`，然后可以`time(); time_ns()`尝试一下
  - 这个应用
    - [[general-programming/debug]]时profiling看什么东西占比时间多
    - 制造[[identifier]]
- pandas中
  - 例如[[rolling]]，[[timestamps]]
# 算法中
- 节省空间
  - [[encode-decode#进制转换]]
  - [[partial-sum]]：线性空间复杂度编码平方
  - 例如[[41-first-missing-positive]]法一
    - 用一个`int`（正负号）表示一个`int`一个`bool`
    - 所有无价值信息（负数）都统一用一个码表示，这也是常见思想
  - 例如[[huffman]]编码树淋漓尽致体现此思想
- 节省时间
  - [[hash]]
- [[trivial-mistakes-in-algo#uniqueness]]
  - 例如[[geometry]]格点三角形题
## 进制转换
- 把一个序列编码成一个数
  - 或相反
  - 呃，你说哪边叫做编码，看具体情况
    - [[naming#命名有时是相对的]]
    - 比如在[[hash]]中，序列变成数就是哈希函数，就是编码
    - 但有时把数编码成十六进制字符串等，比如[[xxd-diff]]
- [[off-by-one-errors]]
  - `[1,1]`在十进制下编码成是`11`，与`[1]`编码成`1`不同
  - `[0,0]`和`[0]`就有麻烦，你不能都0吧
  - 所以说，编码一个序列为数
    - 如果label从1开始而非从0开始，那么不需要编码（记录）长度
      - 也就是这样一来十进制只能编码`1-9`九种label
    - 否则需要记录序列长度，避免0产生问题
  - 当然，可以牺牲一定的可读性，用`1-10`表示十种label，来换取编码效率
    - 这样对于`110`这种三位数，其实含义是原来的`99`
      - 确实没有原来那么直观可读
    - 论证：对于两个不同序列
      - 其长度不同，当然编码不同
      - 其长度相同，那么它们如果用`0-9`编码不同，`1-10`编码还是不同！
# 数学中
- [[parametric-or-not]], [[parametric]]
  - 是否合理？比如[[拟合优度检验]]
- [[sufficient-statistics]]
- [[topological-space]], [[graph-for-topo]]，去除无关要素，只看连通性
## 直角坐标和极坐标
- [[3-calculus]]
- [[normal#symmetry#旋转]]
# [[identifiable-states]]
# 数据科学
- [[normalization#排序]], [[character/quantile]]作为某种编码
- encode浪费一定空间使得深度学习时性质好
  - 二维sin-cos编码表示二维旋转
  - 三维：用6维表示空间中三维旋转，参见[Visual Imitation Made Easy](https://dhiraj100892.github.io/Visual-Imitation-Made-Easy/resources/paper.pdf)
- [[visualization]]时[[color]]相当于用二维直观表示三维
## [[deep-learning-basics]]
- 表示学习 representation learning
- [[autoencoder]]
- [[VAE]]
### NLP
- [[one-hot]]
- [[word2vec]]
- [[nlp-pretrain]]
# 其它
- 精度和[[complexity]]往往需要[[tradeoff]]
  - 例子：[[volatility-for-portfolio]]，用factor和idiosyncratic估计[[cov]]矩阵
# 其它参考
- 参考[[file-format]]，特别是关于“文本、二进制”的部分
- [[xxd-diff]]
- DS/ML中[[dimensionality-reduction]]
- 和[[escape]]有密切关系（“码”不够嘛）
- 把环境抽象成文本序列，如[[docker-file]], [[create-env-from-yaml]]
- [[cryptography-examples]], [[steganography]]是特殊的编码手段，可能保密、安全等
## 盲目encode的坏处
- 有损压缩丢失重要信息
  - 做不出题。参考[[imagination]]
  - 不[[idenpotent]]，如“图压绿了”
  - [[拟合优度检验]]，乱设模型不行
  - 假设空间不够，欠拟合
- 无故增大思维复杂度
  - 例：向量表示成坐标
     - 把向量表示成坐标是通法，但未必简单
     - $\vec a,\vec b$单位向量成45度，何时$k\vec a - \vec b \perp \vec a$
     - 此题不涉及坐标，所以不用坐标更简单