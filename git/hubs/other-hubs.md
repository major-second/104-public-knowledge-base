git和github是什么关系？
- git本身只是一套管理系统，你可以只在本地用，比如[[stash]]，[[reset]]等等
  - 无论用什么托管平台（hub），[[git-basics/installation]]都是需要的
- github是一个托管平台，可以一定程度上理解为网盘。除了github肯定还有其他的提供商
  - 例如你没有代理[[node]]，那就可以找国内的类似物，比如gitee等
  - 例如你在公司内，就要用公司内部的托管平台
  - 例如你要存密码等重要信息（"key"），那就可以用[[keybase]]的hub功能
- 不同hub可以共享同样的[[https-ssh]]公钥。你用一个私钥可以连接许多hub
- 上传镜像操作参考[[fork-private]]（比如国内备份一份墙外的）