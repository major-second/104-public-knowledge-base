$f(x,\theta)=S(\theta)h(x)exp(\sum_k C_k(\theta)T_k(x))$
和[[sufficient-statistics]]的联系：
$h()$乘起来就是[[sufficient-statistics]]里的$h$，$S$乘起来被包在$q$里了
$exp...$会被包到$q$里，所以$\sum T_k$（对各个$k$）是充分统计量
- 均匀分布不属于指数型！注意$f$虽然能写成$I_{[a,b]}(x)\frac 1{b-a}$，但$I_{[a,b]}(x)$并不**只**是$x$的函数，所以不能套$S(\theta)h(x)$