## 缺失值
- [参考](https://zhuanlan.zhihu.com/p/137175585)
## 其它
- [[normalization]]
- [[sklearn]] [文档](https://scikit-learn.org/stable/modules/preprocessing.html#preprocessing)
- 小心[[information-leak]]
- 减某个基础值
  - 使得均值为0
  - 或满足其它目的（排除公共变量，市场影响等）
  - 参考[[data-science/residual]], [[factors-alphas]]
- 有时除以某个“基底”量，进行无量纲化，即$\frac x{x_0}$
  - 例子[[returns]]
  - 但注意[[general-principles/special-case]]除以0的问题
- 过滤异常值
  - [[12-robust]]
  - 强行特判[[general-principles/special-case]]过滤
  - [[pandas-clip]]
  - winsorization缩尾
    - 用[[numpy-basics]]的`np.clip`乃至[[3-linear-regression]]提到的sigmoid函数把两边太高的收一收
    - 可用[[character/quantile]]
  - 参考[[12-robust]]，[[1x1conv]]
- 作用
  - 增大数据所谓“密度”
  - 除了这点还有很多类似于[[normalization#为什么]]的效果，比如减少[[float]]误差, 减少[[gradient-issue]]等
    - 很容易理解增大密度是除了[[normalization#为什么]]外额外的效果
  - 当然也可能丢失信息
- 很多0，个别正负值，可能变成categorical
  - “名义变量”
- 有时想要求数据数字特征满足某些性质
  - 有时要使得[[variance]], [[expectation]]为指定值，有时要使得最大最小值为指定值
  - 通过某种变换，变成正态/均匀分布，参考[[data-science/normalization]]
    - 例子
      - [[data-science/normalization#排序]]
      - [[data-science/normalization#z-score]]
      - [[12-robust]]提到Fisher变换$F(x)=\frac 12 ln(\frac{1+x}{1-x})$就是把某个量变为近似的正态分布
      - [[batchnorm]]
      - 恒正，看起来像$e^X$（其中$X$是[[normal]]），显然应该log
    - 本质上有点[[fit-using-expressions]]嫌疑，唯象！如果能白箱解决还是白箱解决
      - 例如：本质上是$Z+e^X$的，你看到[[skewness]]，显然应该拆出来
      