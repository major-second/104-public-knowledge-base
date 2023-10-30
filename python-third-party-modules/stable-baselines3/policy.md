- 前置[[stable-baselines3/basics]]
- 自己定制policy！[参考](https://stable-baselines3.readthedocs.io/en/master/guide/custom_policy.html)
- 原来的policy往往填简单的字符串`"MlpPolicy"`这种玩意
- 现在你可以自己定义，然后传入相应的类
  - 比如[官网例子](https://stable-baselines3.readthedocs.io/en/master/guide/custom_policy.html#advanced-example)
  - 定义类，这个类需要有特定的属性和方法（参考官网例子！），然后即可传入agent的类如`PPO`，比如官网的`model = PPO(CustomActorCriticPolicy, "CartPole-v1", verbose=1`
- 打断点，在`stable_baselines3/stable_baselines3/common/policies.py`中能看到特定的这些属性、方法用到了什么地方。为什么必须有它们才能满足接口
  - 例如
```python
    def forward(self, obs: th.Tensor, deterministic: bool = False) -> Tuple[th.Tensor, th.Tensor, th.Tensor]:
        """
        Forward pass in all the networks (actor and critic)

        :param obs: Observation
        :param deterministic: Whether to sample or use deterministic actions
        :return: action, value and log probability of the action
        """
        # Preprocess the observation if needed
        features = self.extract_features(obs)
        latent_pi, latent_vf = self.mlp_extractor(features)
        # Evaluate the values for the given observations
        values = self.value_net(latent_vf)
        distribution = self._get_action_dist_from_latent(latent_pi)
        actions = distribution.get_actions(deterministic=deterministic)
        log_prob = distribution.log_prob(actions)
        actions = actions.reshape((-1,) + self.action_space.shape)
        return actions, values, log_prob
```