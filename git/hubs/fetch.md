- `git fetch`相比[[push-pull]]
  - 可以断点续传
  - 更加灵活（如：把远程的fetch下来，不自动更新本地。先观望再merge）
    - 在[[hubs/troubleshooting]]中“用别人的不用自己的”时就用到了`fetch`操作
- 应用：断点续传`clone`较大的库的流程
  - 新文件夹`git init`使得隐藏文件夹`.git`建立（参考[[hidden-files]]）
  - `git fetch <项目地址，以.git结尾>`
    - 可以重复多次，断点续传
    - 完成之后，输出有`FETCH_HEAD`字样，但文件夹中表面上没有东西
  - `git checkout FETCH_HEAD; git remote add <一般填origin> <项目地址，以.git结尾>; git pull <一般填origin> <分支名>; git checkout <分支名>`