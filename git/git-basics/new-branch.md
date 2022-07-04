有时候团队合作时，为了保险和隔离起见，开发时请用自己的branch，确认没问题再发pull request给管理者
- `git branch -m new_name`
  - 参考`git branch -h`帮助[[help]]
  - 结果：`-m, --move            move/rename a branch and its reflog`
- 然后始终用自己的branch
- `git push <一般是origin> new_name`就可以指定push到自己的branch
- 觉得告一段落了，就给团队管理者发pull request（在github或[[other-hubs]]的网页上发）