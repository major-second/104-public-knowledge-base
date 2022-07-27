`pickle`不能传`lambda`函数，module等等。只能传很有限的一些东西
比如`Can't pickle local object`报错
> Classes, functions, and methods cannot be pickled

所以[[be-used]]中用到pickle时，就必须注意不能有复杂东西