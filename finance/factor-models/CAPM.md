# Capital Asset Pricing Model (CAPM)
- [Reference Link](https://en.wikipedia.org/wiki/Capital_asset_pricing_model)
- [Reference Zhihu](https://zhuanlan.zhihu.com/p/60495483)
## Overview
- CAPM is a model used to calculate the expected return on assets.
- $E(R_i) = R_f + \beta_i(E(R_m) - R_f)$, where
  - $E(R_i)$ is the expected return on asset $i$
  - $R_f$ is the risk-free rate
  - $\beta_i$ is the systematic risk of asset $i$, which is a constant.
    - The comparison between $\beta_i$ and 1: $\beta_i$ represents the risk of asset $i$ relative to the market, and 1 represents the risk of the market.
- e.g. (an ideal example, i.e. CAPM is accurate)
  - $R_f = 0.01, R_m\sim N(0.02, 0.01), R_1\sim N(0.02, 0.02), R_2\sim N(0.02, 0.005)$
- An ideal case
  - $R_1-R_f:R_2-R_f:R_m-R_f = 4:1:2 (const)$ for any timestamp
  - On a specific timestamp, $R_m - R_f= 0.005 > 0(bull market),R_1 = 0.03, R_2 = 0.0225, R_m=0.025, R_f=0.01$
  - On another timestamp, $R_m - R_f= 0, R_1 = R_2 = R_m = 0.02, R_f=0.01$
## Alphas
- The original CAPM formula assumes the return on an asset is completely predicted by its beta (systematic risk) relative to the market
- However, many assets have non-zero alphas, indicating that their actual returns deviate from the returns predicted by the CAPM model.
- Compared to the example in [Overview](#Overview), a more realistic case
  - $R_m - R_f= 0.005, R_1 = 0.031, R_2 = 0.022, R_m = 0.025, R_f=0.01, \alpha_1 = 0.001$ (excess return is positive, outperforms the market)
- CAPM is a simplified model, and some factors that are not considered could be "alpha" here, like the factors in [[fama-french]].
  - ref: [[factors-alphas]]
- $\beta_i, \alpha_i$ can be regarded as results of the [[feature-engineering]] process for asset $i$ in terms of data science.
