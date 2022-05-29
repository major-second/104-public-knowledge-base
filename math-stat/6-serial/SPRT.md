前置
- [[6-serial/basics]]

基础
- 考虑类似[[似然比]]的参数空间只有两个元素的情况
- 似然比统计量：两种假设的似然函数之比
$\lambda_n = \prod_{i=1}^n f_2(X_i)/ \prod_{i=1}^n f_1(X_i)$
- 停止法则：$\tau^* = inf\{n:n\ge 1,\lambda_n \notin (A,B)\}$，也就是出现极端就停
- 具体停止法则表达式有时很好计算（比如伯努利、正态等时）