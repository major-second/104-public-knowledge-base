https://blog.csdn.net/qq_34317565/article/details/109257781
参考这个
先`service docker stop`，修改config，重启宿主即可。之后可以正常`docker start <名字>`等等（待验证）
比如改共享内存大小