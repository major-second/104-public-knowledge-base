EDA (Exploratory Data Analysis)，即对数据进行探索性的分析。充分了解数据，为之后的数据清洗和特征工程等提供想法和结论
- 参考
  - 可以先拿文本、excel等粗略翻有所感受，无需一来就上代码（其实不一定方便）
    - 特别多个文件对齐时，直接同时打开多个编辑器是最快的
  - [一个EDA过程](https://blog.csdn.net/AvenueCyy/article/details/104405747)（这个针对非时序数据）
  - [[linux-edit-commands]]初步
  - [[matplotlib/basics]]
- 首先：“外部”：业务知识、自己的理解
  - 一个例子：[这个](https://blog.csdn.net/weixin_42033491/article/details/108104305)中一来的列表
    - 这个针对时序数据
  - 一来是数据的列名（字段名）、类型、含义、示例等基础信息，一目了然列成表，这就是所谓[[metadata]]
    - 也可以根据自己理解往表中列入更多信息，如数据[[category]]，单位（以确保哪些之间可以加减）等
- 其次：“内部”：统计、数据[[visualization]]

- 看什么
  - 先从有代表性的、大部分的入手
  - 对比分析具有不同性质的