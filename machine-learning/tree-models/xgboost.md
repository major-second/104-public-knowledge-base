- [介绍](https://machinelearningmastery.com/gentle-introduction-xgboost-applied-machine-learning/)
# 使用
```python
import xgboost as xgb
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) 

# Specify parameters
param = {'max_depth': 3, 'eta': 0.3, 'objective': 'multi:softprob', 'num_class': 3}

# Convert the dataset into DMatrix
dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test, label=y_test)

# Train the model
bst = xgb.train(param, dtrain, 20)

# Make prediction
preds = bst.predict(dtest)

# Choose the highest probability class for each sample
best_preds = np.asarray([np.argmax(line) for line in preds])

# Print accuracy
print("Accuracy = ", accuracy_score(y_test, best_preds))
```
# 原理
- [参考](https://zhuanlan.zhihu.com/p/562983875)