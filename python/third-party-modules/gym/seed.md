如何去除随机性？使用`.seed()`方法
举例：
```python
>>> import gym
>>> e = gym.make('CartPole-v0')
>>> e.seed(42)
[42]
>>> e.reset()
array([-0.01258566, -0.00156614,  0.04207708, -0.00180545])
>>> e.reset()
array([ 0.00560942,  0.01842265, -0.03590751, -0.0120678 ])
>>> e.seed(42)
[42]
>>> e.reset()
array([-0.01258566, -0.00156614,  0.04207708, -0.00180545])
>>> e.reset()
array([ 0.00560942,  0.01842265, -0.03590751, -0.0120678 ])
```
可以看到设定随机种子后不但之后紧接着的一次能确定，之后的任意多次也能确定