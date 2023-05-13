## 两个重要极限
- $lim_{x\to 0} \frac{sinx}x =1$
  - 应用[[trigonometric-derivative]]
- $lim_{n\to \infty}(1+\frac 1n)^n=e$
  - 扩展：$lim_{n\to \infty}(1-\frac 1n)^n=1/e$
    - 应用：[[2-eval]]中的自助法
## 洛必达
- 洛必达去除对数例题：$lim_{n\to +\infty}e^{n[ln(1-lnn/n)+lnn/n]}$
  - 只需看$lim n[ln(1-lnn/n)+lnn/n] = lim\frac{ln(1-lnn/n)+lnn/n}{1/n}$
  - 洛必达得
$\frac{\frac{1-lnn}{n^2}(\frac 1{lnn/n-1}+1)}{-1/n^2}=\frac{lnn/n\cdot (lnn-1)}{lnn/n-1}=\frac{ln^2n-lnn}{lnn-n}$
  - 洛必达得
$\frac{1/n\cdot 2lnn-1/n}{1/n-1}=0$
  - 综上答案为1
  - 总结
    - 运用[[reduction]]思想。逐步转化成简单的case
    - 利用$limf(g)=f(limg)$
    - 去除对数：适当调整分子分母（比如$lnn/n$不能作为分子，$lnn$能作为分子），使得$ln...$裸露出来，然后洛必达
## 先[[naming#exists]]再列方程
- 典型：出现[[self-similarity]]时
  - 例如[[6-math]]第7题
  - 需要先证明极限[[naming#exists]]（例如单调有界），再设，列方程