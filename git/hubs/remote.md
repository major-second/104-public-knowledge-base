1. 默认：[[clone]]自带`remote`为`origin`
2. 也可以先[[init]], [[commit]]，先没有任何remote，之后再加
   1. `git remote add origin <某某.git>`并`git push --set-upstream origin master`这样
- 还可以多个`remote`
 1. 比如[[other-hubs]]中的`gitee`，`git remote add origin1 https://gitee.com/<一堆>.git`
    1. 注意：这里需要换个名称`origin1`
    2. 可能指定[[port]]用于[[https-ssh]]，例如
         `git remote set-url origin ssh://git@<ip>:<port>...`
 2. `git remote`，`git remote remove`，`git remote set-url`都可以试试，这样[[CRUD]]齐了
 3. 这个链接的[[https-ssh]]选择：参考[[https-ssh]]
 4. [[push-pull]]中`push`不带`-u`，则不改变默认origin，带了就改变