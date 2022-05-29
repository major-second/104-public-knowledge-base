- 一种典型的wrapper：比如自己写的时候，输入一个环境，输出一个环境，有`self.env`这个attribute
常见重载`reset`和`step`，比如下面的。就是改一下输出类型。
```python
from torch import Tensor
from numpy import ndarray
def __init__(self, env):
    self.env = env

def reset(self):
    state: Tensor = self.env.reset()
    return state.detach().cpu().numpy()

def step(self, action: ndarray):
    action = Tensor(action).cuda()
    next_state, reward, done, info = self.env.step(action)
    next_state = next_state.detach().cpu().numpy()
    reward = reward.detach().cpu().numpy()
    done = done.detach().cpu().numpy()
    return next_state, reward, done, info
```
- 为了减少重复造轮子，也可以让你的wrapper继承`gym`里的。比如
```python
class ObservationWrapper(gym.ObservationWrapper):
    def __init__(self, env):
        super().__init__(env)
    
    def observation(self, obs):
        # modify obs
        return obs
```
注意继承之后，wrapper仍然是“输入的是环境，输出的也是环境”