- 前置
  - [[maximum-likelihood#likelihood function]]
  - [[iid]], [[variance]]

[toc]
# score function
- 定义
  - [[maximum-likelihood#likelihood function]]对数似然函数关于$\theta$导数
  - $s(X;\theta):=\frac{\partial logf(X;\theta)}{\partial \theta}$
- 观察
  - 同时和$\theta,X$有关
  - 这里$X$是一维的
## [[random-variable-functions#pdf-continuous]]性质
$\int f(x;\theta)dx=1$
$\frac{\partial}{\partial \theta}\int f(x;\theta)dx=0$
用于推导关于score和Fisher Information的性质
## 均值为0
- 原因: $\int sfdx = \int \frac{f'_\theta}f fdx=(\int fdx)'_\theta=0$
  - 推论：根据[[variance#与$EX^2$关系]]，方差就是平方期望
## 二阶导和一阶导关系
- 参考
  - [[hessian]]
  - [[fisher-information#参数是向量]]
- $\int s''fdx = \int \frac{f''f-f'^2}{f^2}fdx=-\int (s')^2dx$
# fisher information
## 一维
- 对于密度$f(x;\theta)$性质“好”的随机变量
- 其（一维） [score](#score-function)对于给定$\theta$，是只关于$X$的随机变量
- 故可以计算
  - 关于给定$\theta$，$X$不同取值求[[variance]]
  - $I(\theta):=Var[ s(X;\theta)]$
- $\int_E (\frac{dlogf(x;\theta)}{d\theta})^2f(x;\theta)dx$，其中$E$是$f$为正的部分
## 应用
- [[optimal-estimator]]中用$I(\theta)$找界
- 注意此时需要正则化条件$E$恒定
## [[high-dimension]]
### 多个样本[[iid]]
- 定义是$I_n(\theta)=Var(\sum s(X_i;\theta))$
- [[iid]], [[variance#可加性]]
- 所以$I_n(\theta)=nI(\theta)$
### 参数是向量
- 和[[fisher-information#多个样本iid]]是不同方面的拓展
- $l_n:= \sum_{i=1}^n logf(X_i;\theta)$
- $H_{jk}:=\frac{\partial ^2 l_n}{\partial\theta_j\partial\theta_k}$是[[hessian]]
- $I_n(\theta):=-(逐元素对H求期望)$
  - 负号来源
  - 以及为何这个matrix是[[fisher-information#一维]]特例
  - [[fisher-information#二阶导和一阶导关系]]
- $J_n(\theta):=(I_n(\theta))^{-1}$
  - [[1-prob/independent]]时[[general-principles/independent#diagonal]]，从而逆也好求
  - 这个$\hat J_n$地位就是[[cov]]或$\hat {se}(\hat\theta)^2$
    - 所以[[mle-delta-method]]可以拓展到[[multi-mle-delta-method]]
- 适当条件下[[asymptotically-normal]]
  - $\hat\theta - \theta \approx N(0,J_n)$
  - [[general-principles/special-case]]
    - 一维，$\hat\theta - \theta \approx N(0,1/I(\theta))$
      - [[fisher-information#bernoulli-binom#bernoulli]]
      - [[fisher-information#normal]]
    - [[general-principles/independent#diagonal]]情况
# 算例
- [[variance]]查表，参考[[characters-list]]
## [[bernoulli-binom#bernoulli]]
- $f(x;p)=(1-p)^{1-x}p^x$
- $I(p)=Var(-\frac{1-x}{1-p}+\frac xp)=E()^2$
- $=q/q^2+p/p^2=\frac{1}{pq}$
- 参考[[characters-list]]，[[bernoulli-binom#bernoulli]]方差就是$pq$
## [[normal]]
- $f(x;\mu,\sigma)=\frac 1{\sqrt {2\pi} \sigma}exp(-\frac{(x-\mu)^2}{2\sigma^2})$
- $I(\mu)=E[(-(x-\mu)/\sigma^2)^2]=1/\sigma^2$
- $I(\sigma)=E[(-\frac 1\sigma + \frac{(X-\mu)^2}{\sigma^3})^2]$
  - $=\frac 1{\sigma^2}+\frac {3\sigma^4}{\sigma^6}-2\frac {\sigma^2}{\sigma^4}=\frac 2{\sigma^2}$
  - 用到[[normal#moment]]