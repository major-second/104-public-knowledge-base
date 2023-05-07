- 前置
  - [[type-i-ii-errors]]

# 功效
- 功效, power function
  - 对于指定否定域$W$（或称检验法），其$\theta$下肯定的概率$L_W(\theta)$称为OC函数
  - **否定**的概率$1-L_W=\rho_W$称为功效函数
  - 直观含义：检验法奏效，检出了**假设不成立**情况。第二类错误少
  - 类比
    - 功效为[[general-principles/special-case#极限情形]]1时，对应数理逻辑的[[完全性]]
      - 有定理，我就能找到，类比：假设不成立，我就能否定
    - **“正例”对应“假设不成立”**（下同），则直接类比[[2-eval]]的召回率recall
      - 实际上是正例，我就能判定为真，类比：实际上假设不成立，我就能否定
# 水平
- 水平, level, size
  - $sup_{\theta\in \Theta_0}\rho_W(\theta)$：第一类错误概率的上界，称为检验水平（显著性水平）
    - 这个一般都需要低，是一个比较小的数比如0.1
    - [[type-i-ii-errors]]讲到：like a legal trial，一般保证不要错杀
  - 直观理解：如果检验出来不符合假设了，那可不是随口一说。如果你本不该被否定的，那么被这样检出的概率可小了
  - [[all-of-stat/0-metadata]]教材定义：size是这里精确的水平，而level是任何大于等于size的数
  - 类比
    - 水平为[[general-principles/special-case#极限情形]]0时，对应数理逻辑的[[可靠性]]
      - 我说是定理，就是定理，类比：我说假设不成立，就是假设不成立
    - 无法直接类比[[2-eval]]的precision
      - 因为我们现在是[[数理统计学讲义/1-introduction]]中的频率学派
      - 不是[[bayes-inference]]
      - 无法计算“否定假设时，确实应该被否定的概率”
      - 联系：[[confidence-interval#interpretation]]
    - [[general-principles/special-case#极限情形]]：水平为0，所有实际上满足$H_0$的都不会被否定，相当于所有的负例都不会被判正，这时准确率precision为100%
# 联系
- 两者之间有[[tradeoff]]
  - 由两者，定义优良标准[[UMP]]
- 第一类错误我们严格控制，但功效我们只能尽可能希望大，没法严格控制
  - 参考[[UMP]]
  - 两侧地位不对称！所以$H_0$和$H_1$地位倒过来，结论可能不同
  - 那怎么办？你$H_0$是取$\theta\le c$还是$\theta>c$？根据实际情况决定
  - 做假设时就带有倾向性！