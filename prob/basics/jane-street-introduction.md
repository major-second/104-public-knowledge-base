[toc]
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
- 涉及到“意义”，可以参考[[probability-definition]]
- [[random-variable-introduction]]类型：如01，离散，连续等
# Counting
- [[sample-spaces-events#有限情况]]
- 注意有时各个事件不等概率
  - 有理数可以转化为等概率
  - 无理数不行。那就按不等概率看
# Probabilities
- 基本公理、计算规则等，参考[[probability-definition]]
# Independence
- [[1-1-prob/independent]]
- 可使用乘法
- 放回/不放回有区别
# Random Variables
- [[random-variable-introduction]]
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
- 交易的目的：提高期望，降低方差
  - 有时为了一个可以舍弃另一个
  - 色子例子：期望不变，而增大风险，那当然不好
  - 比如可能策略：3 at 4, 10 up.
    - 这样，风险厌恶者可能以3卖给你丢色子机会这样
- 问题例子：包括[[fermi-estimation]]，对[[character/var]]的概念思考等等。非常考察insight
# Adverse Selection
- 交易对手方？
  - 对赌！一方对
  - 对方不关心价格（急买急卖/长期投资）
- 逆向选择概念
  - 买的没有卖的精，你了解更少信息，被对方选择性坑，最后做差的交易
  - 条件概率在此体现重要作用
  - 因此你的交易一成功，就要更新信念
> I don't want to belong to any club that will accept me as a member

- 这个思想：没有说你坑了club，只有club坑你。只有坑的club会找你，所以是“逆向选择”
# Problem Solving Tools
- 自相似
  - 参考[[general-principles/recursion]]
  - 例子：“第一次丢出硬币正面需要多少次投掷”
- Edge cases
  - 一种：用[[general-principles/special-case]]检查正确性
  - 另一种：找最简单的作为[[general-principles/recursion]]出口，[[induction]]起始点等等
# Interview Myths
- 数感，速算，数量级可能有用，但不是那种快速计算乘法
- 我们喜欢直觉，没必要会很多定理
- 不是只有对错重要。敢于问、敢于表达过程，参考[[1-general-principles]]
- 不要非不停说，过于自信。可以思考思考。不要急。可以换位思考其它面试者