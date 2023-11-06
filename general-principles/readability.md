# 程序
- [[comment]]
- 写文档，并考虑[[read-doc]]读文档者感受
- [[general-programming/logs]]
- 遵守约定俗成的东西
  - 例如[[shrc]]提到一来`cd`不可取
  - 例如循环变量命名常用`i, j`，未知数用$x$，[[binary-search]]命名上下界用`ub, lb`或`hi, lo`
  - 例如[[pep8]]这类规范
# presentation
- focus more on your progress since last update
- 参考[[minimum-beamer/README]]
- 参考听众水平，换位思考对方
  - 不能指望短时间把不懂的人讲懂
  - 注意听众有没有follow领域/你的项目等，有没有背景
  - 如果senior已经懂很多，就不用说废话
# 数据
- 参考
  - [[series-dataframe]]做处理
  - [[tabular/source]]
- 明确意义、高还是低好
- 数据可复现性、一致性
  - 格式一致
  - 结果尽量一致
  - [[non-determinism]]怎么办
    - 可用fixed random seed
    - 保证reproducibility
    - 相比多个随机种子取平均，平时跑时更快，当然可能有不[[integrity]]嫌疑
# 表
- 加上有用结果，适当详细化！
  - 特别是不花时间的，你不妨[[general-programming/logs]]出来看看呗
  - 但特别花时间的比如ablation studies不用每次都做
# 图
- 一定要坐标轴说明、坐标轴旁刻度ticks、标题、图例legend等
  - [[matplotlib/basics]]
  - [[axis]]
- 分布图和单个数值的区别，[[encode-decode]]
  - 分布图
    - 更精细，不丢失信息
  - 单个数值和数值构成的表
    - 例子
      - [[数字特征]]
        - [[expectation]], [[moment]]
      - 线性相关性用[[correlation]]概括
      - [[autocorrelation]] acf用halflife概括
    - 有时更直观
      - 特别是初期探索阶段/成果不明显时（1%在表上根本看不出来）
    - 方便做比较。图不好直接比
## phase diagram
- [参考](https://en.wikipedia.org/wiki/Phase_diagram)
## phase portrait
- [[phase-portrait]]
# 文字，caption
- 适当括号解释不常用的或有歧义的词，或者换个说法
- 歧义
  - [[naming#命名有时是相对的]]
  - [[naming#有名字作为交流基础]]
- 明确定语（A的B）