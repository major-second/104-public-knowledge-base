可以先看[[4-probability]]，里面有很多这里的题，我就不重复写了
1. 3.5但是要考虑风险、收益等问题
2. [[dp]]，倒推
   1. 典型扩展题：每次再收1元，[[self-similarity]]
3. [[dp]]，倒推
   1. 注意容易论证如果你第一次愿意开盒，那么之后更加愿意开盒
4. [[mix-strategy]]均衡
5. 
   1. 法一：对数是[[5-martingale-and-random-walk]]，方差越来越大，那么真数肯定最后变成无穷
   2. 法二：相互独立，所以期望乘积等于乘积期望
6. 手推几何分布
7. [[self-similarity]]
   1. 也可直接定义计算
8. 略
   1. [[5-martingale-and-random-walk]]法：每次使得余额是$-n$，如果赢钱就结果比$-n$多，输钱就是$-n$，连赢三次就停
   2. 这样的停止规则产生的是鞅
   3. 所以停止时钱$14-n$期望为0
   4. 当然还需要证明：停止时间期望有限
      1. 联想[[5-brownian-motion-and-stochastic-calculus]]中提到过的：布朗运动到1为止（而不是到$\pm 1$为止），停止时间期望无穷，故也不能简单套用。和这里形成对比！
9.  略
    1.  [[5-martingale-and-random-walk]]法：第一问是赌赢一次收手，第二问是赌赢两次收手
    2.  注意这里的$-yp$意思就是如果赌输，就$-yp$，否则$+y(1-p)=+(1-p)(1p=+p)/p$，这样才是鞅
10. [[bayes]]
11. 需要合理先验
    1.  比如先验1%，那么100次下来，几乎必定是不正常的……
12. [[re-classification]]看每个位置
13. 略
14. 参见15
15. [[bayes]]，$1/3, 1/2, 1/3$
    1.  钻牛角尖：是不是如果两个女孩那么更容易让你知道？
    2.  知道一个女孩的名字，那也就是至少一个女孩嘛
16. [[symmetry]]
    1.  需要给出：有些非工作日并不是周末
    2.  注意第一天是六、天、一都导致第四个工作日是星期四！！坑
17. [[bayes]]
18. [[symmetry]]减去相等情况
19. [[4-probability]] chess tournament
    1.  knock-out tournament: a competition in which a team or player is eliminated once and for all
20. 略
21. with replacement有放回抽样
22. [[5-markov-chain]]
23. [[5-martingale-and-random-walk]]
24. 略
25. [[4-probability]] drunk passenger
26. 略
27. 略
28. 略
29. [[4-probability]]的order statistics
30. 略
31. 
    1. 记号上小心。可以引入$Y=g(X)$从而引入$f_Y$记号
    2. 注意$g(X)\le x$也就是$X\le g^{-1}(x)$
    3. 注意单调性、绝对值等问题
32. 略
33. 略
34. 略
    1.  当然有很多版本。最普通版本：iid方差有限。当然也有不独立的版本
35. 正定的定义
    1.  尼玛坑人呢，应该是半正定
36. 对样本空间中的点赋予不同概率
    1.  原本有的还有，原本没的还没
    2.  后面先不管了todo
37. 略
    1.  注意可以用[[character/var]]的简单性质算出$EX^2$无需积分
38. $M(X)$的cdf是……，所以$M(X)$是均匀分布