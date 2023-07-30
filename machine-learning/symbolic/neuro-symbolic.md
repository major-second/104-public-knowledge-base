- [Neural Symbolic Regression that Scales](https://arxiv.org/pdf/2106.06427.pdf) survey
  1. 把[[activation]]直接换成符号，例如`+, sin, exp`
     1. 显然不本质，需要太多先验，[[gradient-issue]]
     2. 属于[[discriminative-generative#discriminative]]
  2. [[encode-decode]]到连续空间, [[VAE]]
     1. [Grammar variational autoencoder](http://proceedings.mlr.press/v70/kusner17a/kusner17a.pdf)
        1. 是[[discrete-continuous]]手段
        2. 使用grammar CFG 彻底避免生成无效点
        3. 相当于人手动[[encode-decode]]一层，不用原始字符串，而用production rules
        4. 例如：原始SMILES grammar中production rules有100条，一个具体的分子只涉及其中10条，则先人手动把字符串编码成production rules
        5. rules再用[[VAE]]自动编码
        6. 解码时先把连续向量解码成rules，再变回字符串
     2. 可能缺点：不像[[symbolic-regression#bayesian]]一样容易加入simplicity先验
  3. [AI Feynman](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7159912/pdf/aay2631.pdf)
     - 相当于把nn当成超级管用的interpolation方法，给出待推断的landscape再寻找[[symmetry]]等等好性质
     - 这里就有“物理学中常见哪些对称性”这种inductive bias
     - 属于[[discriminative-generative#discriminative]]
- [Neural Symbolic Regression that Scales](https://arxiv.org/pdf/2106.06427.pdf)
  - [[transformer]]
  - train set-to-latent encoder, latent-to-sequence decoder
  - 显然可自动生成sequence和set数据集
- CVPR 2023 best paper
  - [解说](https://www.zhihu.com/question/607381076/answer/3084941484)