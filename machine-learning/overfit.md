- 参考
  - [[2-eval]]
  - 传统统计语言[[p-value-hacking]]
- 现象
  - train高，val低
  - train，val都高，test低
    - 套娃过拟合
    - 所以这是一种学术不端：疯狂过拟合测试集
- 原因
  - [[domain-gap]]
    - 如不满足[[stationary-processes]]
  - 拟合了噪声, [[SNR]]低
  - 假设空间太大，大概率不在你想要的附近
- 如果你疯狂以`test`上的结果为标准，就还是有过拟合嫌疑！
  - [[naming#命名有时是相对的]]，你相当于把`test`当成`validation`
  - [[p-value-hacking]]
# 解决方法
## 数据
- 获取更多数据、更“密集”（[[domain-gap]]更小）的数据
  - 扩增[[augment]]数据
    - 这时往往用[[symmetry]]，如平移旋转翻转
    - 也可以加噪声，这个原理就类似于[[tricks#dropout]]和[[activation]]中random relu等，提升鲁棒性
- [[preprocessing]]
- [[11-feature-selection]]
## 模型
- [[ensemble#bagging]]
  - 注意[[ensemble#boosting]]反而加剧了过拟合
- [[tricks]]
# 参考
- [[7-cross-validation]]提到overfitting is like "file lossy-compression" algorithms