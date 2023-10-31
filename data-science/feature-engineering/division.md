# [[dimensionless]]
- 同量纲相除，制造[[dimensionless]]
- 自身做分母
  - 变化率，[[returns]]
  - 短[[MA]]/长[[MA]]
    - 当期值/[[MA]]当然是特例
- [[normalization#除以标准差]]
- 想表达“稳定地往一个方向移动”，可以考虑$\frac {位移}{路程} = \frac{x_{T+t}-x_T}{\sum_{i=T}^{T+t-1}|x_{i+1}-x_i|}$
- [[imbalance]]及类似物
    - [[VPIN]]: $\frac{\sum |a-b|}{\sum (a+b)}$
    - [[imbalance]]: $\frac{a-b}{a+b}$
    - [[accumulation-distribution-line]]: $\frac{左-右}{总长}$，或说$\frac{左-右}{左+右}$
# 注意分母
## 非负性、非零性
- 非负
  - 本身物理意义非负
    - 路程
    - [[traded-volume]]
    - [[turnover-换手]]
  - 平方、绝对值或其和等
    - [[variance]]
    - [[variance#standard deviation]]
    - 路程也算
- 注意如果可能出现0，还要考虑加一个常数
  - [[nan]]中有提到
  - [[batchnorm]]的官方[文档](https://pytorch.org/docs/stable/generated/torch.nn.BatchNorm2d.html)中也有提到
## 分布稳定性
- 刚刚短[[MA]]/长[[MA]]，分母不够长导致分布有些接近0的boil整个分布，则需要考虑让分母更长