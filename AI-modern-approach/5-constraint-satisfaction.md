- state参考[[2-intelligent-agents]]的representation：这里使用factorized等，不再看成全部indivisible的黑盒
- 有一些通用剪枝法（发现violate the constraints）
## 5.1 Defining Constraint Satisfaction Problems
- 基本要素：变量集，各自定义域，约束（定义域笛卡尔积的子集）
  - 某条约束可能只涉及一部分变量
  - 约束可能枚举出子集，也可能用一定规则（比如$a>b$）生成
- consistent：不违反约束
- assignment：给变量赋值
- 不违反约束的部分（全部）赋值就是部分（全部）solution
- 一般是NP完全。特例好做
- 例子：澳洲地图，任意相邻不同色
  - 于是画出constraint graph，相邻地块连边表示之间存在约束
  - 如果存在超过二元的约束就会有“超图”
- 优势：有时这种表示很自然。剪枝更多。违反时告诉你为什么
- 另一个典型例子：流程安排
  - 可能出现算术和逻辑词复合：disjunctive constraint
- 八皇后也可以看成8个变量的CSP
- 更难的拓展：不再是有限个变量，离散定义域
  - 线性约束很容易解。可以证明非线性约束一般难解
  - 连续定义域，线性规划，运筹学，二次规划……
- 约束的种类
  - 一元：就是限制定义域
  - 二元
  - 任意多元可以引入辅助变量变成二元
  - 或使用Dual graph: 点边地位互换
  - global：包含任意多个（只是习惯说法，别纠结名称，不一定包含所有变量）
    - 例如`Alldiff`
    - Cryparithmetic谜题：“不同字母代表不同数字”
    - 相比暴力二元的好处：简单不易出错。可能引出特制高效算法
  - preference：不绝对，只是觉得……更好
    - COP（约束优化）。线性规划是特例
## 5.2 Constraint Propagation: Inference in CSPs
- [[3-search]]走一步，就是机械地expand一步
  - CSP的搜索树，走一步可能是分类讨论某个变量（多个子节点）
  - 或约束传播（即利用已有信息剪枝减小定义域）（单个子节点）
  - 有时只约束传播就能解决问题
  - 核心思想：local consistency
- local consistency列举
  - 每种consistency往往对应一种传播操作
  - node：直接剪定义域
  - arc（其实就是edge，只不过历史习惯叫arc）：如果某个二元约束使得某变量定义域中某值“彻底没戏”，就剪
    - AC-3算法：维护一个队列，装所有（有向）边，每次针对一个有序对去剪枝，并把所有被剪变量可能产生的影响（一些新的有序对）加进来
      - 如何判断“可能产生哪些影响”？看constraint graph
    - equivalent：不会多解少解。但定义域变小了！
    - 所有domain大小为1：找到解。至少一个domain空：无解
  - path：第三变量$X_k$相对于两个变量$X_i,X_j$而言。如果第三变量定义域中某值使得另外两变量无论怎么取都不能让$X_i,X_k$相关的二元约束和$X_k,X_j$相关的二元约束同时满足，那剪
    - 名字：可以理解成$i-k-j$路径
    - 举例：两种颜色涂3个两两相连的地块
  - $K-$：第$k$变量相比任意选定的$k-1$个变量而言，如果其定义域中某值使得指定其它$k-1$个变量的某个组合时，一定矛盾，那就剪
    - $1-$就是node，$2-$就是arc，$3-$在只有二元约束时是path
    - strong $K-$：$K-$且$(K-1)-$且……直到$1-$
    - 显然对于$n$个变量，strong $n-$能保证有解
    - 没有免费午餐：consistency越强，保证他的开销越大（但是越接近最终解）
    - 实际中：$2-$，$3-$等
- global constraints
  - 有些特制算法：如对于Alldiff简单对比剩余变量数和剩余可取值数
  - 如对于总资源限制resource constraint，可能只看最小值判断是否violate，可能确定某变量取值后看其它变量最小值看是否剪掉
    - 对于整数规划，常常传播上下界。并关注上下界处的类似arc consistency的性质等（bounds-consistent）
- 数独：只arc能解决最简单的，加上path能解决稍难的
  - naked triples：如$\{1,8\},\{3,8\},\{1,3,8\}$，你不知道谁是谁，但反正打包起来干掉了3个数（针对alldiff的特制算法）
## 5.3 Backtracking Search for CSPs
- 这里的expand是多赋值一个变量
- CSP具有commutativity交换性，赋值顺序无关紧要。故树的第一层固定去赋值第一个变量
- backtrack
  - 参考[[backtrack]]
  - 关注伪码：相比简单版的[[backtrack]]中的代码，这里除了先加后删$var=value$在赋值列表，还有先加后删$inferences$在$csp$问题（用来储存一些特别赋值导出的**只有局部能用**的约束传播结论等）
  - 能使用domain-independent heuristics，如关注什么变量，先赋什么值，如何传播，回溯是否多步
- 先关注什么变量：按顺序/随机/剩余定义域小（fail-first，尽快剪）/影响别人多
  - by orders of magnitude: 好出数量级
- 先赋什么值：别影响别人太多（让接下来赋值有更多可能性，fail-last）
  - 为什么这个是fail-last，前面是fail-first？因为每个变量迟早都要涉及，你拖也没用。但是赋值如果尽可能追求成功，还真有可能快点找到解
  - 如果要求找到所有解，那fail-last没啥用
- 搜索过程中的传播
  - forward checking：用arc consistency去除将来变量的定义域中无用值
  - MAC：从forward checking考察的那些有序对开始，然后像AC-3一样如果改了变量定义域就再进一些有序对
    - 相比forward checking更强，相比AC-3不用一来装所有有序对，更快
- 回溯策略：比如可以回溯到最近的造成无解（“背锅”）的变量，而不是傻傻回溯上一个变量（backjumping）
  - 使用forward checking很容易记录哪个变量背锅
  - 不过严格执行forward checking/MAC时是是一定没有backjumping的
  - 更强的跳：conflict-directed backjumping
    - 34导致5无解了，回去变4
    - 什么？4没有其它选择了？而且2限制过4？那么说明23定下来之后，45一定无解。回去变3
    - 什么？3没有其他选择了？而且1限制过3？那么说明……
- no-goods：不良的变量组合模式。可以记录下这种东西作为约束，扩充约束的集合
## 5.4 Local Search for CSPs
- 回忆[[4-local-search]]的complete state formulation，即所有都赋值，可能有violation. 然后爬山/退火减少violation
  - min-conflicts heuristic：选择能使得conflicts数最少的
- 几百万皇后也基本上常数时间搞定
- 约束数/变量数太少或太多的情况都非常容易用local search做。不多不少的critical ratio比较难
- COP显然也可以做
- 出现最后几个顽固conflicts？类比[[4-local-search]]的plateau，也可以用sideways moves
- 禁忌搜索：避免短的环（记住出现过的）
- constraint weighting：虽然要解的是严格约束而不是软约束，但过程中可以赋权，使得plateau有起伏，且机器可学习出哪些约束难
- 还有个优势：online变化（突然某个机场天气坏了）时好用