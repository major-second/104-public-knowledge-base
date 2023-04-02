- 前置
  - [[maximum-likelihood#likelihood function]]
  - [[iid]], [[variance]]
# score function
- [[maximum-likelihood#likelihood function]]对数似然函数关于$\theta$导数
  - $s(X;\theta):=\frac{\partial logf(X;\theta)}{\partial \theta}$
  - 同时和$\theta,X$有关
  - 这里$X$是一维的
  - 对于密度$f(x;\theta)$性质“好”的随机变量均值为0
# fisher information
- 一维
  - 对于密度$f(x;\theta)$性质“好”的随机变量
  - 其（一维） [score](#score-function)对于给定$\theta$，是只关于$X$的随机变量
  - 故可以计算对于某个参数$\theta$的$I(\theta):=Var_\theta s(X;\theta)$
  - $\int_E (\frac{dlogf(x;\theta)}{d\theta})^2f(x;\theta)dx$，其中$E$是$f$为正的部分
- 应用
  - [[optimal-estimator]]中用$I(\theta)$找界
  - 注意此时需要正则化条件$E$恒定
- 高维：[[variance]]可加
  - 所以$I_n(\theta):=Var_\theta(\sum s(X_i;\theta))=nI(\theta)$