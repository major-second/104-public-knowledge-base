出bug除了代码出问题，也可能数据出问题！
- 不同code生成的数据（遵守不同contract的数据）
  - 最难debug的是缺乏类型检查等等（python，还不用typing的那种），然后意义不同的值具有相同类型
- 有随机性的code生成几次数据，没有“对应着”使用
（在需要连续作很多步处理的场景中，如果你第一步用这个种子对应的数据，第二步用那个种子对应的数据，就可能有麻烦）