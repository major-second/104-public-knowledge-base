- 一个随机变量自己
  - [[random-variable-functions#discrete]]
  - $\sum (-plogp)$
  - 根据底不同，所称呼单位不同
# KL Divergence
- $D(P||Q)=\sum p log (p/q)$
  - 注意这里$plogp$符号正，刚刚entropy $plogp$符号负
- continuous KL Divergence
  - $D(f||g)=\int f log (f/g)dx$
## 性质
- 不对称
- 非负性：对比$plnp$和$plnq$
    - 看$lnx$在$p$处导数恰好为$1/p$
    - “[[marginal]]产出相等”
    - 说明$plnp$求和肯定比$plnq$大（各个$q$不和$p$完全相同）