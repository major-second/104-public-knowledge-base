---
title: git基本概念
type: tools
---

## #git 基本概念
### HEAD
这是当前分支版本顶端的别名，也就是在当前分支你最近的一个提交
### Index
index也被称为staging area，是指一整套即将被下一个提交的文件集合。他也是将成为HEAD的子节点的那个commit
### Working Copy
working copy代表你正在工作的那个文件集

### 操作过程
(https://www.cnblogs.com/kidsitcn/p/4513297.html)
当你第一次checkout一个分支，HEAD就指向当前分支的最近一个commit。在HEAD中的文件集和在index中的文件集是相同的，在working copy的文件集和HEAD,INDEX中的文件集是完全相同的。所有三者(HEAD,INDEX(STAGING),WORKING COPY)都是相同的状态，GIT很happy。

当你对一个文件执行一次修改，Git感知到了这个修改，并且说：“嘿，文件已经变更了！你的working copy不再和index,head相同！”，随后GIT标记这个文件是修改过的。

然后，当你执行一个git add,它就stages the file in the index，并且GIT说：“嘿，OK，现在你的working copy和index区是相同的，但是他们和HEAD区是不同的！”

当你执行一个git commit,GIT就创建一个新的commit，随后HEAD就指向这个新的commit，而index,working copy的状态和HEAD就又完全匹配相同了，GIT又一次HAPPY了。