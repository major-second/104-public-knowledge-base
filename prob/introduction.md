- 顶级量化外资Jane Street给出的对概率论的直观、直觉入门
- [文档链接](https://www.janestreet.com/static/pdfs/trading-interview.pdf)
# Randomness
- 色子6个面：古典概型
- one-off future events如明天天气：每个人都有先验判断，贝叶斯学派
  - 实际应用：你要基于你的想法给出恰当判断
- knowable unknowns
  - 如昨天喜马拉雅山天气
  - 如上个人丢的色子的点数
  - 本来可以知道，但你现在不知道
  - 可以用概率语言推理
- 三者当然也有联系：宿命论，推测一切？
- [[random-variable]]类型：如01，离散，连续等
# Counting
- 离散有限等可能
- 如一个色子偶数，两个色子7，等
- 注意有时各个事件不等概率
  - 有理数：可以转化为等概率
  - 无理数：不行。那就按不等概率看
# Probabilities
- 基本公理、计算规则等
# Independence
- 可使用乘法
- 放回/不放回有区别
# Random Variables
- 通俗：把事件attach上数字就是随机变量
- 变量间可能具有关系，旧变量可制造新变量等
# Expected Value
定义、计算、特征函数、大数定律等
# Confidence Intervals
- 描绘有多么不确定（除了一个简单的期望，其它特征）
  - 极差
  - 方差或类似物（看绝对值/平方？）
  - 90%概率在什么范围内？
- 人们往往过于自信
  - 比如[[fermi-estimation]]：德克萨斯有多少出租车？
# Conditional Probability
- 先验，更新，后验
- 条件概率，条件期望
- 不仅是数学问题。如之后的“逆向选择”也提到
  - 参考[[adverse-selection]]
# Making Markets
- 交易
  - 交易标的：这里忽略不管
  - 方向
  - 价
  - 量
- bid to buy, offer to sell
  - I'm 2 bid for 10.
  - I have 10 at 4.
  - 注意哪个是量哪个是价
- 套利：I'm 2 at 4, 10 up.
- 进场order, 退场取消out
  - trade against
  - sold, hit(sell)
  - take 'em, lift(buy)
  - partial, buy 5
  - filled, fully filled
- 