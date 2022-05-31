把public变成private，并复制所有tag和commit信息
```sh
git clone --bare https://github.com/example-user/public-repo.git
cd public-repo.git
git push --mirror https://github.com/yourname/private-repo.git
cd ..
rm -rf public-repo.git
```
这样就把public库变成了private
- 之后这个private库的正常`clone`（而不需`--bare`）就能得到你想要的结果了
- 但是有[[submodule]]时，会比较麻烦
  - `--bare --recursive`并不行
  - 暴力解决办法：直接拷贝子模块
  - 其他办法：todo