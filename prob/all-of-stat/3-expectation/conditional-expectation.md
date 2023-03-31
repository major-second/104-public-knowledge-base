- 前置
  - [[conditional]]
  - [[expectation]]
- $E(X|Y=y)=\int xf_{X|Y}(x|y)dx$
# Iterated Expecations
- 注意每个$y$确定一个$E(X|Y=y)$
  - 所以$E(X|Y=y)$本身也是随机变量，可以有$E_YE(X|Y=y)$
- $E_YE(X|Y=y)=E(X)$
  - 前提是条件[[random-variable-functions#pdf-continuous]]有$f(x,y)=f(y|x)f(x)$