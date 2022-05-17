python有一大堆包可以调，但是怎么取舍呢？
要想清楚这个包能带来什么，代价是什么，如何替代
- 比如做config，有字典-yaml-omegaconf-[[hydra]]这一链条，如果你只使用hydra的compose功能，那完全可以不调它，只用原生（下层）的omegaconf（[[omegaconf/basic]]）。因为hydra的使用限制太多，有很多tricky的东西
- 但是[[interpolation]]（惰性求值），[[resolver]]这些omegaconf的功能，原生yaml没有，所以我们要调omegaconf