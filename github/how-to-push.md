1.On Github's Web, directly click `add a file` and add a file, it will automatically generate command to pull, commit, and push.
2.Download a`Github Desktop` and clone a image to your own host, your changes on your own host will be regarded as`changes`, and you can commit and push them to Github by click some buttons.
3.Do the same things as `Github Desktop` on `VsCode`, reference:"https://blog.csdn.net/qq_25367937/article/details/114271010?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1.pc_relevant_default&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1.pc_relevant_default&utm_relevant_index=2"
4.Use command such as"init","pull","clone","commit -m", and"push", reference:"https://blog.csdn.net/weixin_42449339/article/details/112410926"
In it, you can also learn how to configure public key and private key on Github.

# troubleshooting
push和pull涉及remote托管平台，所以可以参考[[https-ssh]]，[[personal-access-tokens]]，[[settings-and-configurations]]等排除坑
- 比如`OpenSSL SSL_connect: SSL_ERROR_SYSCALL in connection to github.com:443`可能是代理[[node]]挂了
- 比如没有pull，可能不给你push. 需要先pull别人写的代码，merge并解决conflict，再push