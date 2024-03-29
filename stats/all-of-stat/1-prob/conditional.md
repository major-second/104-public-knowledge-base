- 首先$P(B)>0$（注意[[general-principles/special-case]]）
- $P(A|B)=P(AB)/P(B)$
  - 注意
    - 左侧$A$可加右侧$B$不能
    - A, B不能调换。法律场景常见称为prosecutor’s fallacy
- 典型例子：假阳性率不低，真阳性率很低，则检测出阳性也大概率没事（但比原来患病概率大很多）
- 和[[1-prob/independent]]联系
  - 独立时，$P(AB)=P(A|B)P(B)=P(B|A)P(A)$
  - 不独立时分步计算
    - $P(AB)$有时不好算就需要$P(A)P(B|A)$这样算。也就是given $A$（或其它），才能算$B$
    - 例子
      - [[bayes-theorem#total-probability]]
      - [[order-statistics#multivariate]]