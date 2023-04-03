## 平移
- [[conv]], [[rnn]]的假设
  - 这作为他们的inductive bias
- [[autoregressive]]
- [[stationary-processes]]
- [[stationary-independent-increment]]
- 平移不影响[[cov#corr]]
## 旋转
- 或说中心对称
- [[linearity]]圆上三个点题
- 从线变成圆环，从而旋转对称
  - [[4-probability#4.5]] card game
  - [[order-statistics]]
- 利用旋转对称性设计神经网络
- [[正交矩阵]], [[svd]]
- 标准[[normal]]的性质
  - 多元标准正态球对称
    - 角度均匀分布（无论平面角立体角等）
    - 距离参考[[chi-square]]
  - 应用：$f(Z_1>0|Z_1+Z_2>0)$
## 翻转
- 或说轴对称
- [[confidence-interval]]
- [[normal]], [[t]]都是对称的分布
- [[pnl]]
  - 交易品种是否可双向做
  - 如期货，[[binance]]虚拟币可以，可转债不行
- [[正交矩阵]]行列式是-1时为翻转，相比之下前面 [平移](#平移) [旋转](#旋转) 为1
- 偶函数$-t$到$t$积分
  - 例如[[power-rule#速算应用]]
## 轮换
- 或“地位均等”
- 做题时经常“不失一般性设”
- [[transformer]]初始假设地位均等
  - positional encoding补救了一下，要不然这方面先天不如[[rnn]]的inductive bias
- [[weight-init]]中“初始化成一样”造成问题
- [[order-statistics]]
- 交换：[[235-lowest-common-ancestor-of-a-binary-search-tree]]
- 圆上四个点画两条弦，相交概率$1/3$，因为
  - 顺序看只有$1212$才是相交
  - $1221, 1122$都不相交
  - 三种轮换对称各$1/3$
  - 暴力积分做法
  - $P(相交)=\int_0^\pi \frac 1\pi  \frac{2\cdot x(2\pi-x)}{(2\pi)^2}dx=1/3$，也行
    - 这个可以用[[power-rule]]直接看出来积分结果
## 应用
- [[reduction]]
- 快速给出[[general-principles/special-case]]检验
- [[enumerate#pruning]]
  - 特别是 [轮换](#轮换)，我们经常“不失一般性设”
## break
- 有时需要打破对称性，打破僵局，打开局面
1. [[geometry]]点在多边形内题
2. 16个硬币8轻8重，给定0号，判断它是轻是重（3次天平称）
  - 传统想法
    - 1对1
    - 如果相同，再2对2
    - 如果相同，再4对4
    - 则差一次
  - 8对8完全对称分（也是容易想到的）
    - 如果不等那就接下来好搞定（8个，已知轻的比重的多当然可以两次解决）
    - 如果相等又麻烦了
  - 所以神来之笔：7对7！
    - 一来不等
      - 外面重硬币数量肯定0，1，2
      - 根据[[symmetry#轮换]]不妨设左 > 右
      - 左至少4重，否则左3右2外面2矛盾
      - [[reduction]]成：<8个，且至少4个重，称两次，判断待求0是轻是重，这个简单
    - 等：左3重或4重，外面两个等重
      - 待求+同侧1个 == 外面2个
        - 这四个相同的 vs 同侧4个
      - 待求+同侧1个 != 外面2个，不妨设>
        - A和同侧比，如果相等，都是重，如果不等，显然