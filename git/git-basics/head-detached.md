https://blog.csdn.net/u011240877/article/details/76273335
todo：之后整理解说
```sh
git branch temp; \                  
git checkout main; \
git merge temp; \
git status; \
git push; \
git branch -d temp
```
- 重要：在detach状态，如果不加tag或变成临时branch，那么你的修改是很容易丢失的（当然从好处讲，也很容易舍弃）
- `HEAD detached from 0.0.8`并不是说head在`0.0.8`，而是说从那里detach出来，到了别的地方