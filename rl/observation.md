- `Box`
    - 例如：`self.observation_space = spaces.Box(low=-50, high=50, shape=(10,), dtype=np.float32)`
    - 当然，你的env可以在给出observation前，都作[[normalization]]到$[-1, 1]$
        - 归一化场景示例：涉及机器人的，position用3个数表示（三维空间中），具体范围当然跟你的环境有关。
        - 而orientation常用[[四元数]]，范围$[0,1]$
        - 这样的7个数不加处理一把扔进去，肯定不好