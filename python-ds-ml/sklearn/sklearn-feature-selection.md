- 例子
  - `from sklearn.feature_selection import RFECV`
  - `rfecv = RFECV(estimator=model, step=1, cv=StratifiedKFold(2), scoring='accuracy')`
- `StratifiedKFold`分层抽样
- 常见可调参数
  - `n_features_to_select=10, step=20, verbose=True`