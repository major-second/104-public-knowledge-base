- $r(X)=E(Y|X=x)$称为regression function
  - 估计$r$称为regression
  - $Y=r(X)+\epsilon$，其中$\epsilon$是噪声
    - 通过[[conditional-expectation#Iterated Expecations]]可证明$E(\epsilon)=0$
  - 不一定需要知道$r$，能预测新的：prediction / classification
    - [[discrete-continuous]]