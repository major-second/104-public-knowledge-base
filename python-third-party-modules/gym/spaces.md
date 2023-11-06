- 前置[[env]]
- 用法
  - 创建新的space：`from gym.spaces import <种类，例如MultiDiscrete>`
  - 读取：`<env对象>.observation_space`或`<env对象>.action_space`
  - `space`有`.low, .high`等常用属性
- 示例
  - `Box`
      - 例如：`self.observation_space = spaces.Box(low=-50, high=50, shape=(10,), dtype=np.float32)`
      - 例如：`self.observation_space = spaces.Box(low=array([-1,-2,-3]), high=array([1,2,3]), dtype=np.float32)`
  - `MultiDiscrete`
    - 例如：`MultiDiscrete([ 5, 2, 2 ])`：第0个分量5种选择，以此类推
    - 对于这种空间，可以下标取出`Discrete`空间，例如`s[0]`这样
- 应用
  - 在[[stable-baselines3/basics]]中需要指定`.observation_space, .action_space`属性
  - [[gym/wrapper]]往往可以读取unwrapped环境的`observation_space.high`和`observation_space.low`然后做[[numpy-basics]]数组操作，再构造出新的space
      - 例如`FrameStack`中使用`np.repeat`操作
      - 参考[[numpy/reshape]]