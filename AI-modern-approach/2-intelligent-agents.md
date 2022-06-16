[toc]
## 2.1 Agents and Environments
> An agent is anything that can be viewed as perceiving its environment through sensors and acting upon that environment through actuators.

- percept包括所有历史（自然包括自己的信息）
- agent function: percept sequence to an action
    - 外界看：至少可用打表tabulating表示
      - 有随机性？那就打出分布呗
      - 理论上表无限长（除非限制percept sequence长度）
    - 内部看：用程序实现
- agent定义不要教条化（你硬说计算器2+2=4也是，那你赢了）

> In a sense, all areas of engineering can be seen as designing artifacts that interact with the world; AI operates at (what the authors consider to be) the most interesting end of the spectrum, where the artifacts have significant computational resources and the task environment requires nontrivial decision making.

## 2.2 Good Behavior: The Concept of Rationality
- 一般做法：把环境状态打分，看结果说话
  - 有些agent自己给自己打分，有些agent没有（在做对的事但是不知道为什么）
- 环境打分的坑远比想象多，而且从吸尘器例子可以看出一些
  - 比如看结果不看行为是通用原则，否则核酸检测机构永远没有清零动力（
  - 比如平均还是极端？是否风险偏好？这是深刻问题，在吸尘器例子有体现（一直半干净不脏还是一会干净一会脏）
- 理性：基于先验知识、（后验）历史、当前动作，优化（要求的）结果
  - 先验、（要求）结果变，理性的标准可能变
  - 比如要求吸尘器少动
  - 比如房间地图未知
- 理性不是全知全能omniscience（“吃着火锅唱着歌突然……”）
  - expected <-> actual
  - 理性基于up-to-date sequence不能穿越到未来，但是可以调整未来的percept (information gathering, exploration)
  - 不探索，不变化（认为环境完全是*a priori*）往往很难理性（如粪蛋掉了还不知道的鸟，刻舟求剑，驴胡萝卜拉磨等），称为lacks autonomy
## 2.3 The Nature of Environments
- PEAS description: Performance, Env, Actuators, Sensors
- 比如的士自动驾驶。其Actuators有（抽象的）方向盘、刹车等。Sensors有仪表，摄像头
- software agent在纯软件环境中，但未必就简单。如参加有很多真实图片的拍卖
- 一些分类标准
  - Fully observable/Partially observable
    - 比如吸尘器看不到其它格子的情况，就是partially
    - 极端：unobservable，啥也不知道
  - Single/Multi
    - 到底对方是“物”还是“agent”：`The key distinction is whether B’s behavior is best described as maximizing a performance measure whose value depends on agent A’s behavior.`
      - 此时就不太说reflex agent了
    - 更细：competitive/cooperative
      - 而且这个也不是非黑即白
    - multi的一些特色：沟通交流、随机策略等
  - Deterministic? 是否有随机性
    - 此书认为non-deterministic不定量（概率），侧重定性角度。stochastic侧重定量
  - Episodic/Sequential
    - 分成atomic episodes，每个episode一个percept一个action
      - 或者广义一点：$n$个percepts，$n$个actions. 反正不是一直下去
      - rl中常见的episode就是广义的（不是只有一个action，但是前后episode间无关）
    - 否则就是sequential（“序贯博弈”，更难）
  - Static/Dynamic: 环境是否变化
    - 只有metric变化称为semidynamic
  - discrete/continuous：state, time, percept, action等等是否连续
    - `Input from digital cameras is discrete, strictly speaking, but is typically treated as representing continuously varying intensities and locations.`
  - Known: 指的是是否知道物理规律
    - 军棋暗棋：Known, partially observable
    - 不知道按钮功能的fully observable电子游戏：恰恰相反
    - metric不知道也是unknown（和multi-agent联系紧密）
    - 这个严格来说不纯是环境性质，和agent有关（有些agent知道规则，有些agent不知道但可能也能表现好）
  - 最难的就是`partially observable, multiagent, nondeterministic, sequential, dynamic, continuous, and unknown`
    - 的士自动驾驶：除了知道物理规律，其它全沾
      - 欸嘿嘿，你要是不熟悉别国法律，或者从来没在雪天开过车……
- env class: 一系列，取平均（或其它指标），用来eval agent
## 2.4 The Structure of Agents
- $agent = architecture+program$，program前面提过就是用于计算，architecture是硬件（显卡、机器人等）
  - 本书关注program（特别是算法）
- 本书第一个伪码例子要点
  - 定义：`function FOO-BAR(percept) returns an action`
    - 注意大小写
  - `persistent`表示“全局变量”（可能const如table，或非const如percepts列表），下次call function还是它
    - 所以需要memory存储
    - 所以可以学
    - 举例：`rules`, `transition_model`
  - 用`<-`箭头表示赋值
```text
funciton TABLE-DRIVEN-AGENT(percept) returns an action
    persistent: percepts, <comments>
                table, <comments>
    append percept to the end of percepts
    action <- LOOKUP(percepts, table)
    return action
```
- 和[[coroutine]]的联系：agent有一输入port，有一输出port，和环境asyncronously运行，每次都输入后输出给环境（不保证环境停下来等你）
  - 这更加实际
- table实际上不可行。稍微可行一点的就是if-else判断编程，逐个分类讨论
> The key challenge for AI is to find out how to write programs that, to the extent possible, produce rational behavior from a smallish program rather than from a vast table.

### 四类agent
- Simple reflex
  - 去除历史
  - condition-action rule
  - 可以进行剪枝减少ifelse个数
  - 提升理论高度：认为percept -> state -> 匹配rule -> 得到action
    - 这个匹配过程可以是ifelse也可以是机器学习模型
  - 决定action可能需要一些随机性，要不然容易陷入死局
    - 但往往more sophisticated deterministic agents在single agent环境中表现更好
- Model-based reflex
  - 伪码中：相比之前一个percept直接映射出一个state，现在需要结合之前的`最近action, 最近state, transition_model, sensor_model`得到新的state
  - 这里的sensor_model在之前也有，但其余几个在之前没有
  - 这个state不是完美的，也就是个猜测！
- Goal-based
  - 知其所以然：要明白自己改变state是为了达到什么goal
  - 看起来多了结构降低效率，但也更灵活方便修改（相比写死的ifelse）
    - 所以之前如果使用神经网络做reflex，那这里变goal岂不就是Goal-based了？
- Utility-based
  - Goals相对来说比较僵化（二值，happy，unhappy）
  - Utility可以构造utility function方便驱动工作，比较灵活
  - 理论上，其它agent也可以表现得好像是在优化一个utility. 所以理论上所有agent都可以用一个优化算法
  - 执行难度：感知，知识表示，开发优化算法等
  - model-free agent：直接知道utility，不需要model
  - 更难的setting：utility也可以初始不知道
  - 区分utility（人为，不完美）和作为“理性”标准的performance metric
### Learning
- 之前的所有agent都可以变成learning
- 优点：可以泛化，可以在新环境
- 一个普通agent在这里是大agent的一部分（performance element）
- critic根据新进来的信息和某种performance standard改变learning element
  - 这个critic是客观存在的，不是强化学习中可以学的那种critic.
  - 是一些客观东西（类比sensor model），比如“把对方将死是赢了”，“这张图分对了”（监督信号）
  - 目前认为学习需要监督（`outside the agent`）
- learning element根据目前信息改变performance element
- learning element可以制造问题集让performance element探索（而不是呆在舒适区）
- 举例：learning element包括机器学习中的数据集，优化器，随机动作生成器等
  - 数据集，权重，探索的概率、噪音等可以被新的percepts调整（如AdaBoost，强化学习等）
- `Given a design for the performance element, learning mechanisms can be constructed to improve every part of the agent.`：机器学习中有很多可能的参数给你学
- 典型：学习之前提到的model, utility, 乃至直接学reflex规则（决策树？）
  - 学model接近真实往往有好处（不过可能也不能太真实，太耗计算资源）
- percept本身有一部分作为reward/penalty给critic用：类似动物痛等
  - 有时需要人为给这方面监督信号
### 如何表示状态？
- 一对一地（MDP等）
- 分成一些attribute地（CSP等）
  - 两个状态间不是如同“离散拓扑”一样毫无联系！
- 分成复杂结构看影响地（如建图）（FOL，NLP等）
- 以上表达能力越来越强（强的能表达弱的，反之不行）
  - 例如下棋规则，两页FOL规则能表达千页factorized命题逻辑规则，天文数字的打表规则
  - 但推理和学习过程越来越复杂
- 分布式表示：不是简单的放到某块内存，比较鲁棒