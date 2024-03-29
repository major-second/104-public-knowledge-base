- 参考[[expectation]]
- 定义
  - 前提$E|X|^n$存在
  - $n$阶原点矩$E(X^n)$
  - $n$阶中心矩$E(X-\bar X)^n$，如2阶就是方差，大表示波动大
- 存在性
  - 不一定存在（一阶[[expectation]]都有[[cauchy]]不存在）
  - 高阶存在则低阶存在（数分题）
- 设$k_n$表示$n$阶中心矩，则$n$阶标准化矩$k_n/k_2^{n/2}$
  - 3阶就是偏度[[skewness]]
  - 4阶就是峰度[[kurtosis]]
  - 高阶情况，都是长尾代表大，[[convexity]]思想
    - [[skewness]]什么符号，哪边长尾
    - [[kurtosis]]大，两边长尾
- 举例
  - 常常背诵的：[[normal#moment]]
- 应用
  - [[sliding-window]]计算[[variance]], [[normalization#z-score]]等等，只需计算矩，就可推出其它有用量。滑动求和！