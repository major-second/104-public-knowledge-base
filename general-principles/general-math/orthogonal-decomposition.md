- 目的
  - 找到基，相当于[[encode-decode]]方式，编码成用$\mathbb R^n$表示的向量
  - 编码结果[[general-principles/independent]]，特别地，交叉项为0，“互不干涉”，可用勾股定理，等等
# projection
- 勾股定理，平方和关系
## projection-to-a-hyperplane
- 超空间中的向量投影到超平面上
- 原点到超平面距离
  - 参考[[ball-tangent-optimal]]
  - 结论：超平面$\alpha^Tx + b=0,||\alpha||>0$，原点到它距离$|b|/||\alpha||$
- 实例
  - [[multi-ary#定义和计算]]
## projection-to-a-hyperline
- 最常用[[general-principles/special-case]]：hyperline $x_1=\cdots=x_n$
  - $argmin_z \sum (x_i-z)^2=\bar x :=\sum x_i/n$
  - $\sum(x_i-z)^2=\sum((x_i-\bar x)+(\bar x-z))^2=\sum (x_i-\bar x)^2+\sum(\bar x-z)^2$
    - 其中交叉项是常数倍的$\sum(x_i-\bar x)$
    - 注意$\bar x-z=const$
    - 当然为0
- 实例
  - [[MSE#bias-variance tradeoff]]
  - [[转动惯量#平行轴定理]]
  - [[variance#与$EX^2$关系]]
    - $z=0$得到[[moment]]中心矩
    - $z=\bar x$得到[[moment]]原点矩或[[variance]]（“最小”）
  - [[maximum-likelihood-normal]]