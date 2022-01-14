---
title: 原始的score matching
type: knowledge
---

# 原始的 #score_matching
我们想要最小化的Fishel散度如下：
$$\frac{1}{2}\mathbb{E}_{p_\text{data}}[\|\nabla_\mathbf{x} \log p_\text{data}(\mathbf{x}) - \nabla_\mathbf{x} \log p_\theta(\mathbf{x}) \|_2^2]$$
但是我们无法得到$\nabla_\mathbf{x} \log p_\text{data}(\mathbf{x})$，但基于梯度与期望的运算律，我们可以去除这一部分。下以一维数据为例。
将Fishel散度的表达式展开：
$$\frac{1}{2}\mathbb{E}_{p_\text{data}}[(\nabla_x \log p_\text{data}(x) - \nabla_x \log p_\theta(x))^2]$$$$= \frac{1}{2} \int p_\text{data}(x) (\nabla_x \log p_\text{data}(x) - \nabla_x \log p_\theta(x))^2 \text{d}x$$$$= \underbrace{\frac{1}{2} \int p_\text{data}(x) (\nabla_x \log p_\text{data}(x))^2 \text{d}x}_{\text{const}} $$$$+ \frac{1}{2} \int p_\text{data}(x) (\nabla_x \log p_\theta(x))^2 \text{d} x $$$$- \int p_\text{data}(x) \nabla_x \log p_\theta(x) \nabla_x \log p_\text{data}(x)\text{d}x.
$$
由分部积分可得
$$- \int p_\text{data}(x) \nabla_x \log p_\theta(x) \nabla_x \log p_\text{data}(x) \text{d}x\\
$$$$= \mathbb{E}_{p_\text{data}}[\nabla_x^2 \log p_\theta(x)],$$
于是我们最终需要最小化的Fishel散度就和$\nabla_\mathbf{x} \log p_\text{data}(\mathbf{x})$无关了！
推广到高维情形，我们优化的Fishel散度，等价于优化以下目标：
$$\mathbb{E}_{p_\text{data}}\bigg[\operatorname{tr}( \nabla_{\mathbf{x}}^2 \log p_\theta(\mathbf{x})) + \frac{1}{2} \| \nabla_\mathbf{x} \log p_\theta(\mathbf{x})\|_2^2 \bigg] + \text{const}$$
其中$\nabla_\mathbf{x}^2\log p_\theta(\mathbf{x})$即为变量x在函数$\log p_\theta(\mathbf{x})$中的Hessian矩阵。

但是计算Hessain矩阵的开销非常非常大，并且随数据维度上升而飞速增长！对于高维数据来说绝对行不通！

(参考资料：https://ermongroup.github.io/blog/ssm/#hyvarinen2005estimation )