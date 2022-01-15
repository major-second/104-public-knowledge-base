把public变成private，并复制所有tag和commit信息
```sh
git clone --bare https://github.com/example-user/public-repo.git
cd public-repo.git
git push --mirror https://github.com/yourname/private-repo.git
cd ..
rm -rf public-repo.git
```
之后想正常`clone`而非`--bare`也可以。这样就把public库变成了private