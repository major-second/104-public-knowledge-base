# 差分进化算法DE简单示例（来自官方文档）
- [理论](https://blog.csdn.net/jodie123456/article/details/95486270)
- `obj_func`：输入元组，输出待最小化的目标
- `eq, ueq`是约束等式、不等式，输入元组，然后对于`eq`就要求结果为0，`ueq`就要求结果不为0
- `lb, ub, n_dim`都要相应和元组的元数对应
  - `lb`输入`-float('inf')`可能是不行的！必须是有限数
```python
def obj_func(p):
    x1, x2, x3 = p
    return x1 ** 2 + x2 ** 2 + x3 ** 2


constraint_eq = [
    lambda x: 1 - x[1] - x[2]
]

constraint_ueq = [
    lambda x: 1 - x[0] * x[1],
    lambda x: x[0] * x[1] - 5
]

from sko.DE import DE

de = DE(func=obj_func, n_dim=3, size_pop=50, max_iter=800, lb=[0, 0, 0], ub=[5, 5, 5],
        constraint_eq=constraint_eq, constraint_ueq=constraint_ueq)

best_x, best_y = de.run()
print('best_x:', best_x, '\n', 'best_y:', best_y)
```