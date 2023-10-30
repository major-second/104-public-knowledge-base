装完[[linux-kernel]]之后，显卡驱动可能用不了
参考https://github.com/ApolloAuto/apollo/blob/master/docs/howto/how_to_install_apollo_kernel_cn.md
也就是：如果你在装实时内核之前能成功`nvidia-smi`（已经装过[[ubuntu-nvidia-drivers]]），但在装之后用不了了。那么直接从上述链接中
- `cd "$(dpkg -L nvidia-kernel-source-455 | grep -m 1 "nvidia-drm" | xargs dirname)"`（注：`455`要根据你的`nvidia-smi`显示版本进行修改）
- 然后
```sh
sudo env NV_VERBOSE=1 \
    make -j8 NV_EXCLUDE_BUILD_MODULES='' \
    KERNEL_UNAME=$(uname -r) \
    IGNORE_XEN_PRESENCE=1 \
    IGNORE_CC_MISMATCH=1 \
    IGNORE_PREEMPT_RT_PRESENCE=1 \
    SYSSRC=/lib/modules/$(uname -r)/build \
    LD=/usr/bin/ld.bfd \
    modules; \
sudo mkdir -vp /lib/modules/$(uname -r)/updates/dkms/; \
sudo mv *.ko /lib/modules/$(uname -r)/updates/dkms/; \
sudo depmod -a
```
重启系统，`nvidia-smi`正常