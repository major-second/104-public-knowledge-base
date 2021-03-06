[toc]
- "form a path", 通过一系列动作达成：agent称为problem-solving agent, 过程称为search
- atomic representation (更复杂的称为planning)
  - 比如导航去布加勒斯特的例子就很适合atomic
- 本章考虑episodic, single agent, fully observable, deterministic, static, discrete, known的最简单情况（八皇后这种能暴力搜出结果的）
- informed：能估计离目标多远
## 3.1 Problem-Solving Agents
- 搜到布加勒斯特的路线
  - goal：确定objectives（随后再确定action等）
  - problem：确定state, action
    - 例如agent身处哪个城市作为state，城市间移动作为action
    - 肯定需要一定的抽象
  - search：事前offline找到结果
  - execution：执行
- 目前环境假设使得可以确定方案后机械执行
  - 如果有partially observable或non-deterministic：需要branching strategy, contingency plan
- search problem
  - states集合
  - initial state
  - goal states
  - actions: 针对每个state都有一套可能，本章假设有限
  - transition model
  - cost：transition所需cost，本章假设正
    - 零和负都会有些麻烦
      - 环尤其麻烦
    - 加性additive
### Formulating problems
- abstraction: 比如把一系列可能的state, action认为实质相同
  - （开收音机还是不开收音机从A到B）
  - valid：被抽象成一个整体的state集合中任意一个state都有一条具体的path（相当于action）前往属于另一集合的state
  - useful：不能过头，“大象放进冰箱”
    - 说白了，司机自己不需要干预就能在两个城市间单程走。否则就抽象过头了
## 3.2 Example Problems
- standarized
  - grid world: 包括推箱子、吸尘器
  - sliding tile (8-puzzle, 15-puzzle，拼数字)
  - Knuth: 用4通过阶乘，开方，取整等得到5
    - 状态无限，且需要复杂代数结构
- real
  - 机票推荐
    - cost不是单一指标！
    - state需要记录历史，如是否国内航班
  - TSP，实际中可能用来安排公交车等
  - VLSI
  - robot navigation
  - assembly sequencing
## 3.3 Search Algorithms
- 本章算法都是把原来的图当树搜
- 树中可能出现重复的图中节点，但它们对应的path肯定不同
  - 也可能强行指定不重复访问
- frontier separates two regions
  - 内部都被展开了，外部还没访问
  - reached = interior + frontier
- Best-first search伪码
  - node和state概念不同
    - node包含其parent，生成它的action，path-cost
    - state只是`node.`的一个属性
    - parent和action是为了总结解
  - frontier是优先队列，`node <- POP(frontier)`就是把最值得考察的拿出来考察
  - reached是字典（查找表），对于到达过的state找cost最小的node（所以如果新path的cost更小，就会更新`reached[s]`）
  - 什么点值得考察？用个函数$f$表示。之后说
    - $g$之后表示取`path-cost`属性
  - `function EXPAND`有`yield`，所以是某种迭代器，可以被`for each ... in`
    - 参考[[yield]]
- queue此处是广义的，包括优先队列，栈，队列，都有`IS-EMPTH, POP, TOP, ADD`等操作
  - 实践参考[[adapter]]
- cycle和redundant path
  - 概念：所有边正权，则cycle是redundant path（已知非最优的到图中某点的path）特例
  - 检查是否访问过：graph search
  - 否则tree-like（有时也挺好用的，比如在不可能多解的情况，可以节省内存）
  - 有时妥协：只检查cycle（不需要很多内存存reached）
    - 更妥协：只检查短cycle，长的另想办法管管
- performance标准
  - 是否一定能？
    - 有限状态肯定有trivial的完全的搜索算法（graph search）
    - 无限就麻烦了，需要systematically探索无限的state space（例如“螺旋扫荡”二维平面）
    - 无限对无解就更难处理了……
  - 得到path的cost
  - time, space
    - 有时用$|V|,|E|$（顶点数，边数），有时没法具体写顶点边就$d,b$（解的深度，树分支数）
## 3.4 Uninformed Search Strategies
- 比如：完全不知道B离C的直线距离比A近
- Breadth-first：考虑对于所有actions have the same cost，那真的挺好用
  - 即使对无限state也完备，能找到最佳路径
    - 如果不是same cost那不一定最佳
  - 其实就是$f$简单是depth的best-first
  - 相比best-first的具体优化
    - 可以用FIFO代替优先队列
    - reached可以只是一个集合
    - early goal test：拿到node就看是不是goal而不是出队列时再看，反正后面cost也不会变低
  - 时空指数爆炸！
- Dijkstra
  - 直接把$f$定成`.path-cost`，不一定same cost，那就是Dijkstra算法
  - 应该在expand时检查，不在第一次生成某个点时检查
    - 否则可能遗漏更低cost的路径
  - [[shortest-path]]中的Dijkstra不是动态地生成图，而是一开始给你图
  - 所以没有什么generate. 而所谓expand就是“找到到谁的最短路”
  - 做思想实验：每次刚想找`.path-cost`最小的node时，就已经expand好了，表现出来就和一开始有整张图不可区分[[cannot-tell]]. 因为反正你只能看到interior, frontier和外面一层
  - 复杂度：可能一大堆零碎动作，就导致了指数上有$cost/\epsilon$项，指数特别大！
    - 如果same cost那就$cost/\epsilon=d$
    - 本书中$C^*$的star表示最佳的$C$（cost）
  - 完全（按照从小到大顺序systematically）且最佳（根据Dijkstra易证）
- DFS
  - 相当于$f$是负的深度
  - 往往是tree-like（会重复访问）
    - 典型：如不保存全部reached，只保存一条路径上reached，防止循环
  - 不是cost-optimal
  - 对于无限状态，incomplete（可能钻牛角尖）
  - 好处：使用空间小，frontier小（$O(bm)$，$b$是分叉数，$m$是深度）
  - 实际可用，在CSP, propositional SAT, logic programming都有用
  - [[backtrack]]：空间只需$O(m)$（当前到哪了），查询是否reached只需$O(1)$
- depth-limited：超过一定了就不展开。所以不会无限，节省时空，但可能找不到解
  - 可以手工检查短cycle，用limit保证没有长cycle
  - 寻路算法可能用diameter作为limit
- IDS：不断增大limit，memory少且complete且在same cost时optimal
  - 融合之前优点，只不过时间略长
  - 其实时间也没长很多，1110和1230的区别（越大数量级，重复次数越少）
  - 优化版：先breadth-first，没空间了再从当前frontier开始IDS
- bidirectional
  - 两边同时开始搜，$b^{d/2}+b^{d/2}$，省不少空间，适用于单源单汇
  - best-first：需要两个估值函数$f_F,f_B$，哪边值得展开就展开哪边
    - 当然除了best-first也有其它算法
  - frontiers collide就是找到了
    - 实际上是看reached是否有重叠。因为frontier实际上是优先队列不是哈希表
## 3.5 Informed (Heuristic) Search Strategies
- heuristic function: 使用domain knowledge估计$h(n) :=$estimated cost of the cheapest path from the state at node $n $ to a goal state
  - 实际上很多时候知道state就可以估计，不需知道node
  - 如：寻路算法中“直线距离”
- Greedy best-first search
  - 即之前的$f=h$
    - 对比：之前$f$是关注过去，现在是预测未来（启发）
  - 贪心可能导致不最优
  - 启发可能大大加快寻路速度
- A*
  - $f=g+h$，$g$是之前path-cost，$h$是之后（估计）path-cost
  - 和Dijkstra类似，也是generate时不结束，expand才结束
  - $h$的性质
    - admissibility: 乐观估计cost
      - 推导出optimality: 反设找到的不是最优的，则一定有更优的路径，上面有$n$没被展开
      - 则$C^* < C <f(n) = g(n)+h(n) = g^*(n)+h(n)\le g^*(n)+h^*(n)=C^*$，矛盾
      - 其中$\le$来自于adimissibility
    - consistent: 三角不等式（$h(n),c(n,a,n'),h(n')$关系）
      - 这个性质能推出admissibility，因为如果有悲观估计的cost，那三角不等式往下只会越来越悲观
        - 注：这里隐含了$h(goal)=0$
      - 例子：直线距离
      - 更本质的性质：按$f$递增考察，所以可以找到optimal
      - inconsistent有时效率更快。且有时通过一些enhancement能规避其弱点
    - inadmissible时也有一些特殊情况能找到optimal
  - 有时也可能指数爆炸
- contours
  - 容易可视化搜索过程
  - 显然随着搜索，$g$单调（因为cost大于0）
  - 对比刚刚的$f$单调
- optimally efficient
  - 看$f(n)$和$C^*$关系，如果$f(n)<C^*$就称为surely expanded nodes
  - 针对某个consistent $f$，定义optimally efficient: 能展开所有surely expanded nodes
  - $A^*$满足！
  - 至于$f$太大的，$A^*$不管，这就是典型的剪枝提高效率
- satisficing: 不最优，但相对可以
  - 防止$A^*$展开太多，就找satisficing，使用inadmissible heuristic（不一定乐观，但是更精确）
  - 如detour index: 直线距离乘个系数
  - $f=g+Wh$就是weighted A*
    - 理论上：找到的路径在$C^*$和$WC^*$之间，但实际往往很不错
    - Dijkstra: $W=0$, Greedy: $W=\infty$, $A^*$: $W=1$
      - "somewhat-greedy" search
  - 除了刚刚的允许$WC^*$还有一些setting（如允许$\le C$，或无限制）
    - speedy search: 超级贪心超级心急，$f$直接估计剩余步数，尽快找！
- 空间改进
  - frontier和reached不重复存
  - reached中再也不用的就删掉
  - 引用计数，到了一定数就删
- Beam search：frontier只保留$f$最高的$k$个，sub-optimal, incomplete
  - 或：$f$差距小于一定$\delta$才保留
  - 举例：如果Beam中$k=1$（即每次frontier只保留1个），那就一根筋（贪心），很容易找不到解
    - 这个贪心的意思不是greedy best-first search那样“留有余地”，这个贪心把那些非最优的全扔了，之后回不来的
  - [参考](https://zhuanlan.zhihu.com/p/114669778)
- $IDA^*$：cutoff改成$f$，即每次在一个“$f-$contour”内部深搜，每次增大contour
- Recursive best-first
  - 只用linear space
  - 基础是递归DFS
  - 但维护$f\_limit$变量剪枝
    - 即某node所有祖先引出替代方案中最好的那个
    - $min(f\_limit,alternative)$就是在确保剪枝标准是“最好的”那个（即：如果有新的好替代方案，就改成新的）
  - `s.f <- max(s.PATH-COST + h(s), node.f)`其实就是强行保证$f$单调性。如果本来$f$就有单调性那就无需取max了
    - 正因有此单调性，所以在过程中会不断觉得alternative香（有点像“国外月亮圆”“深挖下去全是破绽”）
    - 于是不断反复横跳（润 进 润 出），于是类似$IDA^*$，出现很多重复考察
  - 线性空间复杂度
  - admissible时能找到最优
  - 和$IDA^*$类似的问题：记住的太少，忘记的太多
  - 改进：稍微用多点，memory-bounded $A^*$等
- $SMA^*$：记住很多，实在记不下来就忘记最差的
  - 全相同？按新旧来增删
  - 如果只有一个叶子？说明内存不够了（太深了）
  - 在内存足够时一定complete（太深了就不行）
- bidirectional
  - 两套$f,g,h$
  - 假设admissible
  - $lb(m,n)=max(g_F(m)+g_B(n),f_F(m),f_B(n))$（显然）
  - 但是相比单方向$A^*$，现在具体展开哪个$m,n$就不知道了，因为每个点的$lb$都和其它点有关，不是一元函数
  - 解决方法：维护pair的queue，或$f_2(n)=max(2g(n),g(n)+h(n))$凑合
    - 这种时显然$g(n)>C^*/2$的就不会被展开，所以两边各自伸出一半还是挺直观的
  - 刚刚的$h$基于（一边的）front到其对应的end（goal或initial），其实也可以估计front到另一边front（如对frontier采样或取bbox概括等）
  - 刚刚的$f_2$和admissible $h$下是complete and optimal
  - 效率不一定高（比如heuristic太好，那单向就已经很focused on the goal了）
## 3.6 Heuristic Functions
- 之前一直使用“直线距离”
- 还例如8-puzzle中摆错的数量/曼哈顿距离和（显然都是乐观的）
- 一个评判标准：$b^*$，“等效地”用了几叉树，$N+1=1+\cdots+(b^*)^d$
  - 另一个：相比无启发，降低了等效深度
- 曼哈顿距离和$\ge $摆错数量，dominates，那当然展开的node更少，更高效（除非“平局”时运气不好）
  - 但是你heuristic太难算也不行哈
- 如何自动发明$h$？如放松规则（可以一步到位/可以重叠，给图连更多边），看放松规则下的步数。还能证明consistency
  - 规则中的限制可以被自动去除，从而自动发明$h$
  - 例如本来：相邻空白格子。有两个约束。可以分别去掉或都去掉
  - 还能$h = max(h_1,h_2)$或random选或学习预测哪个$h$最大等（注意后两种更快但不保持好性质）
- subproblem：相当于放松goal，增大goal集合，也能作为$h$
  - pattern databases：存储这种subproblem结果的打表（构建表就是反向从goal搜）
  - 增大考察的pattern数（比如考察`1234****`的复位又考察`****5678`的复位）：边际效用递减
  - max当然可以，相加当然不行
  - 但如果考察1234时认为5678消失（而不是标记成星号）那又可以了（disjoint pattern databases）
- precomputation and landmark point
  - 极端情况：完美缓存所有（如[[shortest-path]]中弗洛伊德算法）
  - 好一些的：设置landmark points，计算所有$C(非地标顶点,地表顶点)$（如果有向图需要再计算反过来的），再取min得到$h$（不是乐观）
    - 如果想要乐观性质，可以$max_L |C^*(n,L)-C^*(goal,L)|$
    - 直观：两边之差小于第三边
  - 好性质：如果真的要经过landmark是最佳（实际中很常见），那$h$是精确的，就真的能找到最佳
  - shortcuts：先计算一些打包好的两点间路径
  - 选择landmark：靠边，散开，结合用户实际等
- 学习搜索
  - metalevel state space：把低级搜索问题中的运行状态当作状态
  - 这些经验可被用来学习（“一些展开是没用的”）
- 学习$h$（估计）
  - `This leads to an inevitable tradeoff between learning time, search run time, and solution cost`
  - 例如手造特征（puzzle中多少个摆错了？多少个倒转？）跑[[multi-ary]]线性回归