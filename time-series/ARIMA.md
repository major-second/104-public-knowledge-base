- 前置
  - [[autoregressive]]
  - [[ARMA]]
- [wiki](https://en.wikipedia.org/wiki/Autoregressive_integrated_moving_average)
- 名称
  - > The autoregressive (AR) part of ARIMA indicates that the evolving variable of interest is regressed on its own lagged (i.e., prior) values. The moving average (MA) part indicates that the regression error is actually a linear combination of error terms whose values occurred contemporaneously and at various times in the past. The I (for "integrated") indicates that the data values have been replaced with the difference between their values and the previous values (and this differencing process may have been performed more than once).
  - 和[[ARMA]]类似可以用[[lag-operator-polynomial]]表示
    - $(1-\sum\phi_iL^i)(1-L)^dX_t=(1+\sum\theta_iL^i)\epsilon_t$
      - 理解：比如$d=1$，则相当于[[naming#换元或简记]] $(1-L)X_t =X_t-X_{t-1}:=Y_t$
- [[general-principles/special-case]]
  - 去除一些字母简记：如$ARIMA(0,1,0)$就是$I(1)$
  - $I(1)$就是[[random-walk]]或with drift，差分是[[white-noise]]
  - $ARIMA(0,0,0)$就是[[white-noise]]
- 实现：[[statsmodel]]