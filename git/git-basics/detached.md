- detached状态：没有对应任何一个（本地或远程）的[[git-basics/branch]]
  - 在detached状态，如果不加tag或变成临时[[git-basics/branch]]，那么你的修改是很容易丢失的
  - 当然从好处讲，也很容易舍弃。所以临时尝试不妨可以这样
  - 注：push时如果弹出报错`undefined`啥的，那你就在detached状态
- `HEAD detached from 0.0.8`并不是说head在`0.0.8`，而是说从那里detach出来，到了别的地方
# 如何脱离detach状态
[参考](https://blog.csdn.net/u011240877/article/details/76273335)，todo：之后整理解说
- 把detached head集成到`main`分支
```sh
git branch temp; \                  
git checkout main; \
git merge temp; \
git status; \
git push; \
git branch -d temp
```
- 这显然是[[temp-solution]]思想
  - 即先临时创建`branch`名为`temp`，`merge`后再删掉
- 注：这里的`main`可能是`master`，参考[[git-basics/branch]]