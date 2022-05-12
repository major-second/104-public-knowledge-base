来自https://askubuntu.com/questions/76081/brightness-not-working-after-installing-nvidia-driver
（关于`.d`文件，请参考[[settings-and-configurations]]）
直接在`/usr/share/X11/xorg.conf.d/10-nvidia-brightness.conf`里，添加以下内容，重启即可
（可以和安装[[ubuntu-nvidia-drivers]]和更改[[grub-menu]]设置的重启一起进行）
```text
Section "Device"
    Identifier     "Device0"
    Driver         "nvidia"
    VendorName     "NVIDIA Corporation"
    BoardName      "Quadro K1000M"
    Option         "RegistryDwords" "EnableBrightnessControl=1"
EndSection
```
或者直接
```sh
echo '
Section "Device"
    Identifier     "Device0"
    Driver         "nvidia"
    VendorName     "NVIDIA Corporation"
    BoardName      "Quadro K1000M"
    Option         "RegistryDwords" "EnableBrightnessControl=1"
EndSection
' | sudo tee /usr/share/X11/xorg.conf.d/10-nvidia-brightness.conf
```
（注：不能直接`echo`重定向否则报错没有权限）
参见[[tee命令]]