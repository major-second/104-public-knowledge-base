把public变成private，并复制所有tag和commit信息
```sh
git clone --bare https://github.com/example-user/public-repo.git
cd public-repo.git
git push --mirror https://github.com/yourname/private-repo.git
cd ..
rm -rf public-repo.git
```
之后想正常`clone`而非`--bare`也可以。这样就把public库变成了private
- 但是有子模块时，会比较麻烦（`--bare --recursive`并没有用）。
  - 暴力解决办法：直接拷贝子模块
（todo）