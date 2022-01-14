（关于`.d`文件，请参考[[settings-and-configurations]]）
直接在`/usr/share/X11/xorg.conf.d/10-nvidia-brightness.conf`里，添加以下内容，重启即可
（可以和[[ubuntu-nvidia-drivers]]的重启一起进行）
```text
Section "Device"
    Identifier     "Device0"
    Driver         "nvidia"
    VendorName     "NVIDIA Corporation"
    BoardName      "Quadro K1000M"
    Option         "RegistryDwords" "EnableBrightnessControl=1"
EndSection
```
来自https://askubuntu.com/questions/76081/brightness-not-working-after-installing-nvidia-driver