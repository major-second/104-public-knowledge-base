$\phi[t/x]$记号：公式$\phi$中自由出现的$x$变成$t$
- 例如$P(x)[y/x]$就是$P(y)$
- $\forall xP(x)[y/x]$还是$\forall xP(x)$
  - 注：这种“无实际作用的代入”在[[natural-deduction]]中可能大有用处
  - 例如$\forall x P(x)\vdash^{ND} \forall x\forall xP(x)$是正确的
  - 此处$\forall x P(x)$也是$\forall xP(x)[y/x]$，这里$y$不在假设出现，也不在$\forall x P(x)$出现。所以满足$\forall I$的条件

“代入自由”：代入时没有“撞外面量词枪口上”
- 比如$\forall y P(x)[y/x]$，就不自由