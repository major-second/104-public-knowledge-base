## Transformer理论基础
- [基础](https://blog.csdn.net/Tink1995/article/details/105080033)
- [如何理解positional encoding中使用三角函数](https://www.zhihu.com/question/347678607)
- [有先验乃至只有先验的注意力](https://zhuanlan.zhihu.com/p/459231092)
## 使用`torch`的实践
版本：`1.9.0`
### 层层拆包
- 最外层`nn.TransformerEncoder`，其由多个`nn.TransformerEncoderLayer`组成
- `nn.TransformerEncoderLayer`最主要模块是`nn.modules.MultiheadAttention`
- 其中主要用到`F.multi_head_attention_forward`
### 主要计算过程
- `F.multi_head_attention_forward`中
- 首先计算出和形状有关的各个整数。注意`head_dim * num_heads == embed_dim`，要求整除
  - 例如：`query.shape`为`(5, 4, 2048)`，表示每个句子5个token（词），每个batch 4个句子，每个词的“词向量”2048维，此时若注意力“多头”数为8个头，则每个头256维
- 接着过线性层。过线性层之前，`q, k, v`都是`(5, 4, 2048)`，且`q is k, k is v`（这就是所谓“自注意力”），但接下来通过一个线性层，把`q, k, v`变成三个新的`(5, 4, 2048)`向量（此时它们不同了）
- 然后reshape为`(5, 32, 256)`，即“多头”注意力和原本的`batch`是同一“地位”，都是某种意义的“批量”！
- 然后核心步骤（注释原文`(deep breath) calculate attention and out projection`可还行）
  - 主要是`_scaled_dot_product_attention(q, k, v, attn_mask, dropout_p)`函数
  - 其中计算注意力的核心是`attn = torch.bmm(q, k.transpose(-2, -1))`
    - `bmm`是批量的矩阵乘法，第一维是batch，而后面两维就$X_{a\times b}Y_{b\times c} = Z_{a\times c}$，就是矩阵乘法
    - 目前`B`是32，而`E`是256，也就是某句子中每个词在注意力的每个头处拥有维数为256的query表示和key表示，通过内积确定注意力大小
    - 因此对于目前的计算，`attn`结果是`32`个$5\times 5$方阵
  - 计算主体之后，如果由于训练需要，要强行进行上/下三角形状的注意力（“注意不到未来”等），可以在`attn_mask`处把一些地方加上负无穷，之后过`softmax`就会变成`0`
  - `softmax`沿着`dim=-1`做，并注意到矩阵形状`Nt, Ns`（虽然此处`Nt==Ns`），这就说明含义是每个`target`词要把总和为1的注意力分配给5个`source`词
  - 计算完成了注意力矩阵，`softmax`后，把它再使用`bmm`乘以`v`，就得到了计算结果。含义在注释中有：`(B, Nt, Ns) x (B, Ns, E) -> (B, Nt, E)`
## 拓展
`attn_mask`除了简单赋予一些负无穷把一些地方设为0外，还可以设为其它，加入其它先验信息。例如对角、靠近对角处给正数就是让离得近的那些更加被注意到等