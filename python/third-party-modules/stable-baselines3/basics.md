- 前置
  - 至少需要`python=3.7`
  - 安装：`pip install stable-baselines3`
  - 了解[[env]]
- 使用：参考[教程](https://stable-baselines3.readthedocs.io/en/master/guide/quickstart.html)
  - 注：`render`的要求比较麻烦，不想要就不要

```python
import gym
from stable_baselines3 import A2C
env = gym.make("CartPole-v1")
model = A2C("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10000)
obs = env.reset()
for i in range(1000):
    action, _state = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    env.render()
    if done:
        obs = env.reset()
```
- `.learn`可能不够灵活，可以分别使用`.collect_rollouts`和`.train`等函数
- 使用[[tensorboard]]只需在初始化`A2C`对象时加`tensorboard_log="./logs"`这种关键字参数