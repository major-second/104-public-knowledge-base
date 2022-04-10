https://hydra.cc/docs/intro/
在omegaconf基础上有一些实用功能。比如多个config group，每个group出一个字典树子节点，compose成config. 这样可以把config文件数量从$\prod x_i$变成$\sum x_i$
目前的缺陷：
- `hydra.main()`包裹的函数没法正常传出返回值。只能用`nonlocal`之类的曲线救国
[这个方法](https://stackoverflow.com/a/60674339)可行。这里的空list和nonlocal变量起到了同样作用