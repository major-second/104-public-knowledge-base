---
title: gradient field入门教程
type: knowledge
---

# 为什么需要gradient field
考虑现有 #生成模型 ，可分成两类：

## 基于似然的模型
即基于最大似然估计，直接对目标分布的概率密度进行建模。
如：自回归模型
(https://blog.csdn.net/shigangzwy/article/details/69525576),
标准化流模型(https://zhuanlan.zhihu.com/p/165577850), 
VAE(https://www.sohu.com/a/226209674_500659)等
![](images/似然模型1.png)
缺陷：标准化常数难以处理，因此需对模型进行限制；
或者需要对最大似然的条件参数进行近似(VAE,假设正态分布条件Ｚ)

## 隐式生成模型
即概率分布由对样本的采样过程去隐式表示的模型。
如GAN！
![](images/隐式生成模型1.png)
缺陷：需要对抗训练，这是出了名的不稳定！超级容易崩坏！

## 我们的方法
不是对概率密度进行建模，而是对概率密度函数的对数的梯度建模！即建模
$$\nabla_\mathbf{x} \log p(\mathbf{x})$$
至于为啥更好呢，且听本文细细道来~




