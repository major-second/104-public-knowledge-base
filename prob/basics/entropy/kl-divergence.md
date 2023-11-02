- 前置
  - [[kl-divergence]] = [[cross-entropy]] - [[entropy]]
    - [参考](https://zhuanlan.zhihu.com/p/389179483)
# 定义
- $D(P||Q)=\sum p log (p/q)$
  - 注意这里$plogp$符号正，[[entropy]] $plogp$符号负
- continuous KL Divergence
  - $D(f||g)=\int f log (f/g)dx$
## 性质
- 不[[symmetry#轮换]]
  - 但两个方向同时为0或不为0
  - 因此在[[parametric]]中有identifiable概念：任意两个不同参数的KL散度不为0
- 非负性：对比$plnp$ [[entropy]]和$plnq$ [[cross-entropy]]
    - 看$lnx$在$p$处导数恰好为$1/p$
    - “[[marginal]]产出相等”
    - 说明$plnp$求和肯定比$plnq$大（各个$q$不和$p$完全相同）