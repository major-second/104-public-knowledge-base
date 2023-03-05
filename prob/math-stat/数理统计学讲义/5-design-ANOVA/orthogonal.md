一共$n$行，$m$列，相当于$n$个数据点，$m$维的feature
“正交”的意思是任意两个feature在试验设计时没有不该存在的相关性（比如对于男生总是赋予方案1比较多）
- 举例$$\left(\begin{matrix}1&1&1\\1&2&2\\2&1&2\\2&2&1\end{matrix}\right)$$，你看任意两列，都很漂亮，四种组合各出现一次
- 直观依据：$y_{ijl} = \mu + \alpha_i +\beta_j + \epsilon_{ijl}$，$\epsilon$是独立同分布正态误差
  - 直观上$\hat \alpha_i = \bar y_i - \bar y,\hat \beta_j = \bar y_j-\bar y$
  - $cov(\hat\alpha_i,\hat\beta_i) = cov(\bar y_i,\bar y_j)-cov(\bar y,\bar y_i)-cov(\bar y,\bar y_j)+var(\bar y) = n_{ij}/n_in_j-n_i/nn_i-n_j/nn_j+n/nn=0\Leftrightarrow nn_{ij}=n_in_j$时，无关（用了[[cov]]常用性质比如[[transform]]）
- 记号：刚刚的称为$L_4(2^3)$
  - $L_n(s_1\times s^{m-1})$当然就意为有一个feature有$s_1$种选择，其余有$s$种选择