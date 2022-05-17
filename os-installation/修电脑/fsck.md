https://askubuntu.com/questions/1103629/error-on-boot-dev-sda6-unexpected-inconsistency-run-fsck-manually
https://www.cnblogs.com/machangwei-8/p/10353614.html
文件系统损坏（可能和[[dual-boot]]时[[bit-locker]]有关）
在黑命令行，`fsck -f <出错的设备>`
- “设备”是`/dev`下属的文件，参考[[linux-devices]]
- `fsck`是修复，但有风险。参考上面的链接
- 出错的是谁？
  - 可能直接提示
  - 可能系统自动进入所谓`emergency mode`，需要`journalctl -xb | grep "fsck failed" -C 5`看是谁错了（参考[[find-grep]]）