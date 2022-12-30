- 前置
  - [[powershell/basics]]
  - [[escape]]
  - [[wsl]]
- windows的[[powershell/basics]]中，`wsl`命令（不是linux系统中的命令）
  - 可用于[[silent]]操作[[wsl]]
- 例：直接`wsl`
    - 这可以和[[link]]结合，从而在桌面一个快捷键直接进入linux终端
    - 参考本文件夹`wsl.ps1`
- 例：`wsl -e echo 1`
  - 注意`wsl -e 'echo 1'`不行（可能被当成整体了）
  - `wsl -e bash -c 'echo 1'`可以
- 例：`wsl --set-default Ubuntu-20.04; wsl --list; wsl -e uname -a`
- 例：`wsl -e bash -c 'echo -e "[boot]\\nsystemd=true" | sudo tee /etc/wsl.conf'`，直接一键[[wsl-systemd]]
  - 当然也可以进行其它[[silent]]操作
  - 注意powershell [[escape]]一次，[[echo]] [[escape]]一次，共2次
- 多行
```powershell
wsl -e bash -c '
for (( i = 0; i < 5; i++))
do
 expr $i \* 5
done
'
```