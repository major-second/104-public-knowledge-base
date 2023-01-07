1. 默认：[[clone]]自带`remote`为`origin`
2. 也可以先[[init]], [[commit]]，先没有任何remote，之后再加
   1. `remote add origin <某某.git>`并`git push --set-upstream master`这样
   2. 这样还可以多个`remote`
      1. 比如换个名称`origin1`，比如[[other-hubs]]中的`gitee`，`git remote add origin1 https://gitee.com/<一堆>.git`
   3. `git remote`，`git remote remove`，`git remote set-url`都可以试试，这样[[CRUD]]齐了
   4. [[https-ssh]]选择：参考[[https-ssh]]