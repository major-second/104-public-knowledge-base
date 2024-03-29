- [参考](https://zhuanlan.zhihu.com/p/40415008)
# BGD, SGD, MBGD
- 梯度（单点/部分/全部）*学习率=更新的量
- 非Adaptive的，可能导致[[gradient-issue]]问题，[[nan]]等，参考[[normalization]]
- 非深度学习也可用比如[[3-linear-regression#对数几率回归]]
# Momentum
- 动量，惯性思想。稳定，摆脱局部，更快等
- Nesterov: 在当前速度决定的终点处求导
# 其它
- AdaGrad: 涉及多的参数，梯度平方积累多，分母大，更新变慢。缺点：让更新量过早变为0
- RMSprop: 用梯度平方的衰减平均值$E[g^2]_t = \gamma \cdot E[g^2]_{t-1} + (1-\gamma) g_t^2$，避免梯度积累到导致分母太大，也能反映参数出现频率相对关系
## Adam
- 前置
  - [[moment]]
  - [[deep-learning/optimization#Momentum]]
- 结合动量+RMSprop思想
  - 速度（“一阶”）和梯度平方（“二阶”）都做衰减平均
    - [[estimation]]
- 另外去除“偏置”
  - 因为初始化0向量，就导致所有一阶二阶项都初始就引入了向0“偏置”的误差。只有不断衰减，才能使初始的0影响足够小
  - 具体地：进行一次“衰减平均”，则0“占比”$\beta$；进行3次“衰减平均”，则0“占比”$\beta^3$
  - 所以bias correction是$\hat x_t = x_t / (1 - \beta^t)$这种，和时间有关
- 平时一般都用Adam
- 一个优点：适用于不稳定目标函数
  - 不稳定目标函数
    - 指的是目标函数的梯度在不同的位置变化很大，导致学习率难以选择，[[gradient-issue]]
    - 这里不稳定不是随机过程中不平稳，不是说函数随epoch动态变化
      - 参考[[stationary-processes]]
    - todo待确认
  - 原因：Adam可以自适应地调整学习率，从而更好地适应不同的目标函数
# 二阶
- 无需超参，直接根据二阶项给出最优点。但计算量大
- 拟牛顿法：不需精确计算Hessian的逆矩阵
- 实际上往往不如Adam
- Adam在某种意义上可以看成“用对角矩阵代替精确的海瑟，然后求逆”