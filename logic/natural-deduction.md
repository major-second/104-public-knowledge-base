自然演绎系统
- 其符号可以参考[[example-doc/README]]在latex中打出
- 当然也可以用分数线和`\quad`命令，即$\frac {\frac {c\quad d}a}b$凑合一下

核心概念：推演。具有（可能）许多假设，一个结论
- 单独的一个公式$\phi$是一个**假设和结论都是$\phi$的**推演（规则名：$A$）
- 相比[[hilbert]]系统，相当于“只有规则，没有公理”。
  - 规则例如$\to E:\frac{\frac D\phi \quad \frac {D'}{(\phi\to \psi)}}{\psi}$
  - 名称含义：$I$引入，$E$排除
- $[]$记号：纯粹就是个记号，先不管它有什么含义
  - 推演中一些公式加上$[]$，是什么意思？
    - 首先，加上$[]$的公式不再认为是假设（“不需要你，我也能得到某某结论”）
    - 其次，推演加上$[]$不一定再是推演（但可能是推演的一部分）
      - 注意“推演加上$[]$”作为另一个推演的一部分相比刚刚的$\to E$，区别是：
      - 刚刚是“一行因一行果”，现在是从$[]$开始的多行因一行果
      - 但是用树结构，同样都可以用根节点表示，形式上可以没有区别。只要自己不混淆即可。参考[[ast]]（抽象语法树）
    - 最后，有个简便记号。为了简便表示“推演加上$[]$”，如果是$\frac D\psi$的所有假设中$\phi_0$加$[]$，就可以写作$\frac{\frac{[\phi_0]}{D}}{\psi}$（不一定是推演）
  - 举例：$\to I:\frac{\frac{[\phi_0]}{D}}{\frac{\psi}{\phi_0\to\psi}}$
    - 用到的假设是集合是：$D的假设-\{\phi_0\}$
    - 可能用于推出“公理”（无需假设的结论）
      - 但是不一定能推出无需假设的结论。因为$D$的假设可能不止一条
    - 为了清晰，刚刚最下方横线右侧可以标记$(\to I),1$，且在$[]$右上角标注1
    - 即：“根节点标规则名。用数字远程连根节点和叶子”
    - 从这个例子可以看出：相对于不加$[]$，加了$[]$有某种“临时前提、临时假设”意味（区别于普通的假设）
- 否定相关规则：
  - $\neg I$：树叶是$[\phi]$（但假设的集合中无$\phi$），推出矛盾的二者，就有结论$\neg \phi$
    - 记作：$D的假设-\{\phi\} \vdash^{ND} \neg \phi$
  - $RAA$：方向相反（相当于“反证法”），直觉主义逻辑没有这一规则
- “无效果的$[]$”：$D$的假设集本来就没有$\phi$，那么你想要$\frac {[\phi]} D$，实际上就是完全没变
  - 应用在$\to I$上，就有$\psi\vdash^{ND}\phi\to \psi$
  - 应用在$\neg I$上，就有$\phi \wedge \neg \phi \vdash^{ND}一切公式$
- [[zero-order-logic]]：增加等词$\dot =$的引入和消去规则
  - 引入：凭空自己等于自己
    - 看来自然演绎系统所谓“没有公理”也只不过是个说法而已
  - 消去：相等即可“替换”（等价替换）
- [[first-order-logic]]
  - $\dot = E$中要求[[substitution]]代入自由
  - $\forall I$
    - 首先有$D\vdash^{ND} \phi[t/x]$
    - 其次$D$中假设**不以$t$为自由变元**（“凭空冒出$t$”）
    - 还要求$t$不在$\phi$出现
      - 其实本来不自由出现加上[[substitution]]代入自由即可
      - 但是可简单粗暴要求“不出现”
        - 不出现则不自由出现
        - 不出现则没有约束的“枪口”所以当然代入自由
    - 所以，有两类典型错误
    - 一种是$t$在$\phi$自由出现了，表现是“有些$t$没变回$x$”，比如$\frac{0\dot = 0}{\forall x(x\dot = 0)}$
    - 一种是$D$假设有$t$，$t$不是“凭空冒出”，例如$\frac{\frac{[x\dot =0]}{\forall y(y\dot = 0)}}{x\dot = 0\to \forall y (y\dot = 0)}$
      - 看起来第一行被$[]$了而不是假设
      - 但是你要想，你在考察第一条线时，“当时第一行还没被$[]$”
      - 是在第二条线时，才被……
      - 所以在第一条线$\forall I$时，$x\dot = 0$是假设
      - 所以$x$不是“凭空冒出”
      - 不能把$x$换$y$引入$\forall$
  - $\forall E$：“代入自由”时进行“替换”（类比等价替换）
  - $\exists I$：“代入自由”时反向“替换”（和$\forall E$看起来“相反”）
  - $\exists E$
    - 第一个树枝：假设中有$\phi[t/x]$，能推出$\psi$
      - 直观意义是“任何一个$\phi[t/x]$都能推出$\psi$，那么我存在一个具体的$t$，就……”
      - 类似$\forall I$，$t$必须凭空冒出。具体地
          - 对于这个树枝这边，除了$\phi [t/x]$，其他假设不出现$t$
          - $t$不在$\psi$出现
          - 也就是从$\psi$的假设到$\psi$，只需要额外加入$\phi[t/x]$即可
          - $t$“既不影响因也不影响果”
      - 且类似$\forall I$，$t$不在$\phi$出现
    - 然后第二个树枝：能推出$\exists x\phi$
    - 那就得到了$\psi$
    - 典型错误
      - $\frac{\exists xP(x)\quad [P(y)]}{P(y)}$：$t$在$\psi$（“果”）出现
  - 看起来
    - $\forall E,\exists I$联系紧密（都是考虑单个项替换）
    - 另两者联系紧密（都是考虑“凭空”$t$，直观上也就是“全部某某”都要满足）
    - 换句话说$\forall$容易应用（消去），难以引入。$\exists$相反