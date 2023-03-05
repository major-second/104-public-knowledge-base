- 前置[[sample-spaces-events]]
- 定义（概率测度）：三条公理
  - 任意事件概率非负
  - 和为1
  - （可数）个不交事件概率可加
- 有时无法定义这样的测度，如$\mathbb R$上
    - `The two common interpretations are frequencies and degrees of beliefs`
    - 对应频率派，贝叶斯派
- 由定义得到的一些性质
  - $P(\emptyset)=0$
  - $A\subset B \Rightarrow P(A)\le P(B)$
  - $0\le P(A)\le 1$
  - $P(A^c)=1-P(A)$
  - $A\cap B = \emptyset \Rightarrow P(A\cup B) = P(A)+P(B)$
- 更多性质
## 容斥原理
## continuity
- 事件不断包含（单调增），$A_n \to A$，则概率也趋向
- 证明：把$A$拆成一系列无交并，用可数可加性