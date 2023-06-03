[toc]
# sin
- 正弦定理
- $sinA/a=sinB/b=sinC/c$
- [[齐次性]]，例如等式两侧$sinA,sinB$同时变成$a,b$
# cos
- 余弦定理
- $a^2=b^2+c^2-2bccosA$
- $cosA = \frac{b^2+c^2-a^2}{2bc}$
- 分子分母[[齐次性]]
# 三角形面积公式
- $2S=absinC=bcsinA=acsinB$
- 和[[trigonometric-in-triangle#cos]]里的$bccosA$有一定关系，注意不要混淆
- 推论$\frac{2S}{(a^2+b^2-c^2)/2}=tanC$
# 内角和
- $A+B+C=\pi$
- $sinC=sin(A+B)$，结合[[trigonometric-equalities#和角公式]]等
- 结合“锐角”“钝角”等，可得$A=\pi-B-C>\pi/2-C$等不等式
# 例0
- 问题
    - ![](trigonometric-in-triangle-0.png)
    - 锐角$\triangle ABC,\angle A<45\degree$，$D$在三角形中，$\angle D=4\angle A, BD=CD$，$E,C$关于$AB$对称，$B,F$关于$AC$对称
    - 证明$AD\perp EF$
- 思想
  - [[reduction]]到已知量。使用各种等量代换
    - [[trigonometric-in-triangle#sin]]
    - [[trigonometric-in-triangle#cos]]
  - [[齐次性]]
- 过程
    - 设$E$到$AD$垂足$E_1$
    - 设$F$到$AD$垂足$F_1$
    - $EF\perp AD\Leftarrow E_1=F_1\Leftarrow AE_1^2-DE_1^2=AF_1^2-DF_1^2\Leftarrow AE^2-DE^2=AF^2-DF^2$
    - $BD=CD=d=a/2sin2A,惯例设a,b,c,则只需b^2-a^2-d^2+2adcos\angle EBD=c^2-a^2-d^2+2ad cos\angle FCD$
    - $\Leftarrow \frac{b^2-c^2}{a^2}sin2A=cos(2C-\frac \pi 2+2A)-cos(2B-\frac \pi 2+2A)$
    - $=sin(2C+2A)-sin(2B+2A)=2cos(C+B+2A)sin(C-B)$
    - $\Leftarrow (c^2-b^2)sinA=a^2(sinCcosB-sinBcosC)$
    - [[齐次性]] $\Leftarrow (c^2-b^2)a =a^2(\frac{c(a^2+c^2-b^2)}{2ac}-\frac{b(a^2+b^2-c^2)}{2ab})$，成立！
# 例1
- ![](trigonometric-in-triangle-1.png)