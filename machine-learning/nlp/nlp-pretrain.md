- [参考](https://zhuanlan.zhihu.com/p/370859857)
- 前置
  - [[encode-decode#深度学习相关]]
  - [[autoregressive]]
  - [[transformer]]
# GPT
- Generative Pre-Training
- [参考](https://zhuanlan.zhihu.com/p/403469926)
- 应用
  - [[chatgpt]]
  - [[waitlists]]
- 预训练时
  - [[autoregressive]]单向预测下一个词
  - [[maximum-likelihood]]
  - 使用[[transformer]]的decoder生成词
# BERT
- 标题：`BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding`
- [参考](https://zhuanlan.zhihu.com/p/51413773)
- 预训练步骤
  - 第一步深度双向预测，给前后文挖空，预测中间
  - 第二步区别是否连续的语句（二分类）
- 相比 [GPT](#gpt)
  - 双向[[transformer]]，是encoder，所以说是预训练encoder
  - [GPT](#gpt)，单向，decoder
- BERT本质就是一个encoder，所以可参考[[word2vec]], [[one-hot]]等