- 洛必达去除对数例题：$lim_{n\to +\infty}e^{n[ln(1-lnn/n)+lnn/n]}$
  - 只需看$lim n[ln(1-lnn/n)+lnn/n] = lim\frac{ln(1-lnn/n)+lnn/n}{1/n}$
  - 洛必达得
$\frac{\frac{1-lnn}{n^2}(\frac 1{lnn/n-1}+1)}{-1/n^2}=\frac{lnn/n\cdot (lnn-1)}{lnn/n-1}=\frac{ln^2n-lnn}{lnn-n}$
  - 洛必达得
$\frac{1/n\cdot 2lnn-1/n}{1/n-1}=0$
  - 综上答案为1
  - 总结
    - 运用[[化归]]思想。逐步转化成简单的case
    - 利用$limf(g)=f(limg)$
    - 去除对数：适当调整分子分母（比如$lnn/n$不能作为分子，$lnn$能作为分子），使得$ln...$裸露出来，然后洛必达