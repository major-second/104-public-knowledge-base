https://blog.csdn.net/u011240877/article/details/76273335
（临时，之后整理）
```sh
git branch temp; \                  
git checkout main; \
git merge temp; \
git status; \
git push; \
git branch -d temp
```
有个要点：在detach状态，如果不加tag或变成临时branch，那么你的修改是很容易丢失的（当然从好处讲，也很容易舍弃）