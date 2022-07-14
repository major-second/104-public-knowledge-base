`from collections import defaultdict`
- 然后比如`d = defaultdict(list)`，`d[<任意键>]`就默认是`[]`了
- 此时可以直接`append`，省略了初始化步骤
- 例如`d = defaultdict(list); d[1].append(0); print(d)`
- 结果是`defaultdict(<class 'list'>, {1: [0]})`