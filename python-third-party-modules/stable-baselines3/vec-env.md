- [官方文档](https://stable-baselines3.readthedocs.io/en/master/guide/vec_envs.html)
- `DummyVecEnv`：单线程。只是表现上是一个`VecEnv`（用作接口、调试等）
- `SubprocVecEnv`：实用的
  - 举例
```python
env_fn = lambda: MyEnv()
env_fns = [env_fn for _ in range(5)]
env = SubprocVecEnv(env_fns)
example_env = env_fn()
```
- `env`是实际可用来并行的，`example_env`则是一个实例，用于取出其中静态方法，`observation_space`属性这种东西