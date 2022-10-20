- 前置
  - 至少需要`python=3.7`
  - 安装：`pip install stable-baselines3`
  - 了解[[env]]
- 使用：参考[教程](https://stable-baselines3.readthedocs.io/en/master/guide/quickstart.html)

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