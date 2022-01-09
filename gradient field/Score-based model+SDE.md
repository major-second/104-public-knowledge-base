---
title: Score-based model+SDE
type: knowledge
---

# Score-based SDE模型
根本思想：我们之前讨论了多级噪声的情形。现在，我们考虑噪声的级数趋向于无穷大的情况。
这时，随着噪声的不断增长，数据在时间维上被逐渐扰乱，即一个连续时间随机过程。而这样的随机过程，是一个随机微分方程(SDE)的解。

数据被逐渐扰乱的过程如图：
![](images/扰动.gif)

(SDE是一个大坑！见 https://zhuanlan.zhihu.com/p/108866971 )

## 使用SDE扰动数据
定义如下形式的SDE:
$$
\mathrm{d}\mathbf{x} = \mathbf{f}(\mathbf{x}, t) \mathrm{d}t + g(t) \mathrm{d} \mathbf{w} \tag{1}
$$
其中$\mathbf{f}(\cdot, t): \mathbb{R}^d \to \mathbb{R}^d$是向量函数，称为漂移系数(drift coefficient), $g(t)\in \mathbb{R}$是函数，称为扩散系数(diffusion coefficient), $\mathbf{w}$是标准布朗运动。
这个式子刻画了数据向量X随着时间推移，可以表示为两种运动的叠加，一种是确定的函数f导致的运动，另一种是随机的布朗运动，乘以一个与时间相关的系数。

令$p_t(\mathbf{x})$表示数据向量X在时间t下的概率密度，其中$p_0(\mathbf{x}) = p(\mathbf{x})$为数据的原始分布。
经过充分长的时间T后，$p_T(\mathbf{x})$被扰动到接近一个易处理的纯粹的噪声分布$\pi(\mathbf{x})$，称其为先验分布。

作为一个例子说明，定义以下SDE：
$$
\mathrm{d}\mathbf{x} = e^{t} \mathrm{d} \mathbf{w} \tag{2}
$$
此即 [[gradient-field]] 中定义的多级噪声$\mathcal{N}(0, \sigma_1^2 I), \mathcal{N}(0, \sigma_2^2 I), \cdots, \mathcal{N}(0, \sigma_L^2 I)$, 其中$\sigma_1 < \sigma_2 < \cdots < \sigma_L$为几何级数，当 $L \rightarrow +∞$ 时的极限情况。

## 倒向SDE生成数据
类似于[[gradient-field]]中退火MCMC采样，对于无穷多噪声尺度，可以利用倒向随机微分方程(reverse SDE)来类似的倒转扰动过程，以从随机噪声中生成样本。
像这样：
![](images/倒转.gif)

在我们的问题中，倒向SDE由下式给出：
$$
\mathrm{d}\mathbf{x} = [\mathbf{f}(\mathbf{x}, t) - g^2(t) \nabla_\mathbf{x} \log p_t(\mathbf{x})]\mathrm{d}t + g(t) \mathrm{d} \mathbf{w} \tag{3}
$$
(别找了，没有证明)
你没看错！为了求解这个式子，我们需要的恰好就是$\nabla_\mathbf{x} \log p_t(\mathbf{x})$！这就是score function!
其实也不奇怪，因为本来就是从离散推广到连续，核心还是一样的！

正逆过程的对比：
![](images/正逆过程.jpg)

## score matching
现在的问题，也就是求$\mathbf{s}_\theta(\mathbf{x}, t)$，以最小化：
$$
\mathbb{E}_{t \in \mathcal{U}(0, T)}\mathbb{E}_{p_t(\mathbf{x})}[\lambda(t) \| \nabla_\mathbf{x} \log p_t(\mathbf{x}) - \mathbf{s}_\theta(\mathbf{x}, t) \|_2^2]
$$
注意我们要最小化的是在整个时间分布[0, T]中L2 loss的期望，其中$\lambda(t)$是与时间相关的权重。可以使用[[denoising score matching]]或 [[sliced score matching]]来做这件事。

通过score matching得到$\mathbf{s}_\theta(\mathbf{x}, t)$后，用$\mathbf{s}_\theta(\mathbf{x}, t)$替换(3)式中的$\nabla_\mathbf{x} \log p_t(\mathbf{x})$，使用数值SDE求解器求解即可。

## Predictor-Corrector samplers
我们可以使用 [[gradient-field]] 中MCMC方法来优化从SDE求解器中得到的trajectory.
根本思想：已知样本$\mathbf{x}(t) \sim p_t(\mathbf{x})$,使用SDE求解器预测$\mathbf{x}(t + \Delta t) \sim p_{t+\Delta t}(\mathbf{x})$，并通过我们训出来的$\mathbf{s}_\theta(\mathbf{x}, t + \Delta t)$校正 $\mathbf{x}(t + \Delta t) $.



