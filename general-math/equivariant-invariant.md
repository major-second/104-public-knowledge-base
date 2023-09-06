# 概念辨析
- equi等，in不，variant变
- equivariant等变性：不是“不变”
  - $f(g(x))=g(f(x))$，不是$f(g(x))=f(x)$
- [参考](https://zhuanlan.zhihu.com/p/41682204)
    > CNN是既具有不变性，又具有等变性。 可以这么理解，如果我们的输出是给出图片中猫的位置，那么我们将图片中的猫从左边移到右边，这种平移也会反应在输出上，我们输出的位置也是从左边到右边，那么我们则可以说CNN有等变性；如果我们只是输出图片中是否有猫，那么我们无论把猫怎么移动，我们的输出都保持"有猫"的判定，因此体现了CNN的不变性。
# equivariant
- [wiki](https://en.wikipedia.org/wiki/Equivariant_map)
- [[linearity]]常见
- [[maximum-likelihood#equivariance]]
# invariant
# 应用
- [[principles-for-dl-models]]