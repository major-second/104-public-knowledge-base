前置：
- [[env]]

## 典型用法
- 我们这里的wrapper是一种典型的[[python/wrapper]]：比如自己写的时候，输入一个环境，输出一个环境，有`self.env`这个attribute
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
## 现成
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
- 来看一个现成轮子：
```python
>>> import gym
>>> env = gym.make('CartPole-v0')
>>> env.reset()
array([-0.02699422, -0.04428904, -0.03518551, -0.04217034])
>>> env.step(0)
(array([-0.02788001, -0.23888924, -0.03602892,  0.23920688]), 1.0, False, {})
>>> from gym.wrappers import FrameStack
>>> env_s = FrameStack(env, 3)
>>> env_s.step(0) # 需要先reset才能使用，否则报错如下
Traceback (most recent call last):
    ...
    assert len(self.frames) == self.num_stack, (len(self.frames), self.num_stack)
AssertionError: (1, 3)
```
我们通过[[seed]]去除随机性，可以看到wrap之前和之后env的密切联系
```python
>>> env_s.unwrapped.seed(42)
[42]
>>> array(env_s.reset())
array([[-0.01258566, -0.00156614,  0.04207708, -0.00180545],
       [-0.01258566, -0.00156614,  0.04207708, -0.00180545],
       [-0.01258566, -0.00156614,  0.04207708, -0.00180545]])
>>> array(env_s.step(0)[0])
array([[-0.01258566, -0.00156614,  0.04207708, -0.00180545],
       [-0.01258566, -0.00156614,  0.04207708, -0.00180545],
       [-0.01261699, -0.19726549,  0.04204097,  0.30385076]])
>>> env_s.unwrapped.seed(42)
[42]
>>> env_s.unwrapped.reset()
array([-0.01258566, -0.00156614,  0.04207708, -0.00180545])
>>> env_s.unwrapped.step(0)
(array([-0.01261699, -0.19726549,  0.04204097,  0.30385076]), 1.0, False, {})
```
查看[源码](https://github.com/openai/gym/blob/master/gym/wrappers/frame_stack.py)，发现返回的observation不是numpy数组，但是通过[[numpy/magic]]即可得到数组（也就是`array(返回对象)`是numpy数组