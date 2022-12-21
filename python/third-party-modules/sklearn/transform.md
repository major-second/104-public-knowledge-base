- 对数据进行变换
  - 先`<model>.fit(train_X)`，然后`X_prime = <model>.transform(X)`
  - 或直接`X_prime = <model>.fit_transform(X)`
- 是数据的preprocessing, 可参考[[tricks]], [[feature-engineering]]等
- `StandardScaler`（均值0方差1）
```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```
- `MinMaxScalar`
```python
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
```
- 类似用法还有`QuantileTransformer`等（保序，全部使用[[quantile]]作为feature）
- [[11-feature-selection]]
```python
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression
model = LinearRegression()
rfe = RFE(model, 3)
rfe.fit(X, y)
X_selected = rfe.transform(X)
```
- [[pca]]
  - 注意很有可能需要先normalize，否则基本上就是看哪个维度方差大hhh
```python
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca.fit(X)
X_transformed = pca.transform(X)
print(pca.components_)
print(pca.explained_variance_ratio_)
```