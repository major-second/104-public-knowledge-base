[toc]
# 辅助角公式
- $Asinx+Bcosx=\sqrt{A^2+B^2}sin(x+\phi)$
  - $cos \phi = A/\sqrt{A^2+B^2}$
  - $sin \phi = B/\sqrt{A^2+B^2}$
  - $A$ [[trivial-mistakes-in-math#非零]]时，$x=arctan (B/A)$
- 常用特例：$sinx+cosx = \sqrt 2sin(x+\pi/4)\in [-\sqrt 2, \sqrt 2]$
# 六边形图
```
  sin cos
tan  1  cot
  sec csc
```
## 余角关系
- $sinx=cos(\pi/2-x)$，横线
## 平方和关系
- $sin^2x+cos^2x=1$
- $tan^2x + 1=sec^2x=1/cos^2x$
- $cot^2x+1=csc^2x=1/sin^2x$
- 倒三角形
## 倒数关系
- $1/sinx=cscx$
- $1/cosx=secx$
- $1/tanx=cotx$
- 六边形对角线
## 来源
- 六边形中相同方向“平移”表示乘或除相同量（[[imagination]]）
# 和角公式
- $sin(a+b)=sinacosb+cosasinb$
- $cos(a+b)=cosacosb-sinasinb$
- 记忆方式
  - 口诀“撒抠加抠撒”等
  - [[trigonometric#几何意义]]
# 积化和差
- 可利用[[trigonometric-equalities#和角公式]]推出
- $2sinacosb = sin(a+b)+sin(a-b)$，同号的变成2倍，异号抵消
  - 是[[symmetry#相同项]]
  - 参考[[binomial#奇偶]]
- 类似写出其它几条
  - $2cosasinb = sin(a+b) - sin(a-b)$
  - $2cosacosb = cos(a+b) + cos(a-b)$
  - $2sinasinb = -cos(a+b) + cos(a-b)$
# 和差化积
- 首先$A,B=a+b, a-b$，其中$a=\frac{A+B}2,b=\frac{A-B}2$
- 所以利用[[trigonometric-equalities#积化和差]]可得
  - $sinA+sinB=2sin\frac{A+B}2cos\frac{A-B}2$
  - $sinA-sinB = 2cos\frac{A+B}2 sin\frac{A-B}2$
  - $cosA+cosB = 2cos\frac{A+B}2cos\frac{A-B}2$
  - $cosA-cosB = -2sin\frac{A+B}2sin\frac{A-B}2$
- 助记口诀
  - 帅+帅=帅哥
  - 帅-帅=哥帅
  - 哥+哥=哥哥
  - 哥-哥=负嫂嫂
# [[齐次性]]
- 关于$sin,cos$的
  - $tan2\alpha = \frac{2sin\alpha cos\alpha}{cos^2\alpha-sin^2\alpha}=\frac{2tan\alpha}{1-tan^2\alpha}$
  - $cot2\alpha = \frac{cot^2\alpha - 1}{2cot\alpha}$
- [[trigonometric-in-triangle]]