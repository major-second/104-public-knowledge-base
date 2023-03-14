# geometric
- $P(x)=(1-p)^{x-1}p, x=1,2,...$
  - [[jane-street-introduction]]有提到
- 意义：$p$概率成功，到成功需要几次尝试
- 求期望：[[jane-street-introduction]]提到的[[self-similarity]]
- 求方差：参考[[character/var]]，需要求$EX^2$
  - 而这个也不简单，[参考](https://zhuanlan.zhihu.com/p/166653762)
  - 主要思想是对$q$积分一下把$x^2q^{x-1}$中的一个$x$抵消掉
# nega-binom
- 定义方面有些微妙的地方：有时容易混淆“成功需要几次尝试”和“成功需要几次失败”，但不本质
- 求期望方差方法：可[参考](https://zhuanlan.zhihu.com/p/166653762)
- 法一：直接写出定义，利用组合恒等式以及自相似性
- 法二：母函数/特征函数
- 法三：看成独立的若干个几何分布随机变量相加