`from collections import defaultdict`
然后比如`d = defaultdict(list)`，`d[<任意键>]`就默认是`[]`了。可以直接`append`，省略了初始化步骤