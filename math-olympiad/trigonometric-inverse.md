- $arcsin$
- $arccos$
- $arctan$
# 求导
- 反函数求导
# 例题
- $f(x)=arcsin(1-x)+arccos 2x$值域只需要单调性
  - 定义域$[0,\frac 12]$
- $f(x)=arcsin(1-x)-arccos 2x$值域需要求导
  - $f'(x)=-\frac 1{\sqrt{1-(1-x)^2}}+\frac 1{\sqrt{1-4x^2}}$
  - $g(x):=\frac 1{\sqrt{1-x^2}},f'(x)=g(2x)-g(1-x)=0$
  - $2x,1-x\in [0,1]$, $g$单调，故$g(2x)=g(1-x)\Rightarrow 2x=1-x,x=\frac 13$