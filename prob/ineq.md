## 两个基本
- Markov: $tP(X\ge t)\le EX$，相当于分两段估计
  - ==非负==
- Chebshev: $t^2P(X^2\ge t^2)\le E(X^2)$
  - 平方，则不要求非负了
  - 变种：平移一下，变成$t^2P(|X-EX|\ge t)\le \sigma^2$
- insight: 大家的关注点都是"tail"（偏差大的那些）
### markov拓展到知道很多统计量
- 很多阶矩？naive想法：$min \frac{EX^m}{t^m}$
- 那[[generating-function]]不也是一组（无穷个）统计量嘛？这个function输入数输出统计量。你也可以$P(X\ge k)\le inf_{t>0} e^{-tk}Ee^{tX}$（“切诺夫”）
## 关于正态分布的特例
动机：不初等不行。要用初等近似（asymptotic，即比值极限为1）
- 进一步：保持以上条件且为上界/下界