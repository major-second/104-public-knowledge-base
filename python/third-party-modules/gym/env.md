## 调用现成
### 初体验
```python
>>> import gym
>>> env = gym.make('CartPole-v0')
>>> env.reset()
array([-0.04959694,  0.01267547, -0.02225354,  0.02826855])
>>> env.render()
True
```
出现图片![](cartpole.png)
### `.step()`
```python
>>> env.action_space
Discrete(2)
>>> env.step(0)
(array([-0.01208408, -0.18500268,  0.01701187,  0.2858684 ]), 1.0, False, {})
>>> env.step(1)
(array([-0.01578414,  0.00987257,  0.02272923, -0.00140094]), 1.0, False, {})
>>> env.step(2) # Discrete(2)说明只有两种可能action
Traceback (most recent call last):
  ...
AssertionError: 2 (<class 'int'>) invalid
>>> for i in range(100):
...  _ = env.step(1) # 避免print出许多obs, done等输出
...  _ = env.render() # 避免print出许多True
```
可以看到不停`1`意为一直往右