- 前置[[git-basics/branch]] [[commit]]
- 常见自己搞branch开发，然后提PR合并到main (default) branch等
- 自己的branch往往可以[[push-pull#push]] force，但肯定一般的main不建议
- 自己branch刚刚push完，上github网页相应库页面可以看到建议（……最新push了……）
- [Update a pull request](https://www.burntfen.com/2015-10-30/how-to-amend-a-commit-on-a-github-pull-request)
  - `git commit --amend` + force push，可以做到“reviewer要求修改，我简单修改一下”，[参考](https://shengyu7697.github.io/github-update-pull-request/)
    - [[commit]]
  - 也可以直接在同一个branch上新增commit
- 和[[github-issues]]关系：[参考](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue)
  - 可以自动关联PR和issues，通过PR后自动close issue
  - 在PR的
    - [[commit]] message
    - 或 description
    - `close` [[github-issues]]编号（`#`开头）
    - 即可关联
- Review
  - 自动：例如本地`just mypy`这类命令行跑一下（你本地不跑，上云还得跑）
    - 自动不通过就没有手动了
  - 手动：设置Reviewer有哪些，这些人会自动收到邮件等
# [[merge]]
- 常见merge后删除[[remote]]的branch
  - 此时本地可以选择删除本地+“本地显示remote”的对应branch使得简洁
  - 否则有时可能有confusing 现象，比如明明已经merge，因为remote已经删除，所以显示没有merge，而且[[push-pull#pull]]也不动