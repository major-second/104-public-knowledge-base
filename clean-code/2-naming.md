---
title: 有意义的命名
type: programming
---

[toc]
# 2 有意义的命名
本篇是[[clean-code/0-metadata]]读书笔记第2章部分。
- 名副其实！用注释补充？不好。自己长一点？好！
  - `elapsedTimeInDays`
  - 简洁度？即使简洁，也可能很模糊！！没有明确意义。`List`是什么？`[0]`是什么？`4`魔数是什么？怎么使用返回的列表？
  - 问题本来应该是代码回答，而不是注释回答。“自明”
- 不要写容易和语境混淆的变量名。不要误导变量类型（`list`这种），提防相似度高的变量名，提防`O,l`等字母
- 不要为了区分而区分（`class -> klass`，太糟糕了）
  - `a1,a2,product,produceData`，太糟糕了。没有提供human-readable区分，只提供machine-readable区分！
- 使用读得出来的。`ymdhms`读作yah-mudda-hims，不好！`Timestamp`，好！
- 长名称，搜得到，不要自造编码系统
  - 名字长短和作用域大小对应（比如循环计数器可以用`i,j,k,m`）
  - 如果没有约定，`moneyAmount`，`accountData`，纯属多余
  - 没必要的语境也不好（长度适中）
- 编码系统：不便发音，增加负担。历史原因：长短重要，编译器不做检查。如今匈牙利语命名法多余！
  - 有些场景（比如抽象工厂），是否编码更有争议
- 类名，对象名，名词
- 方法名：动词（比如`deletePage`或`save`）
  - `get..., set..., isPoseted`：常见规范
  - 明确！例如使用描述了参数的静态工厂方法名，`Complex.FromRealNumber(23.0)`
- 一一对应！一个概念多个名字，多个概念一个名字都不好
- 主要看谁在读！目标导向，为人着想
  - 解决方案领域（和计算机科学、数学更相关）或所涉问题领域
  - 不要炫耀你的聪明。要让别人明确（不要**egocentric**）
  - 不要耍宝抖机灵