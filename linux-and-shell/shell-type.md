- 有些种类的`shell`不能自动`source` [[shrc]]
  - 比如交互式的（像直接`bash`命令进去的）会自动`source` [[shrc]]
    - 但直接`bash 1.sh`这样并不会
      - 当然，你的`bash 1.sh`如果是在交互式`bash`中跑起来的，那还是能用[[6-env]]，但是这还是因为你之前交互式`bash`的`source`
      - 如果你先`bash`再改[[shrc]]再`bash 1.sh`，则修改不生效（[[refresh]]思想）
    - 这样的一个合理之处：比如我们都知道[[proxy-basics]]往往比较慢，所以可能需要`unset http_proxy; unset https_proxy; ./setup.sh`
      - 你如果非交互式时也自动运行`~/.bashrc`就糟了（
  - 比如`bash -c`不会，`bash -ic`会
    - 这一点在[[wsl-command]]中需要了解
    - 在[[docker-file]]中也提到`bash --login -c`相比`bash -c`不同
  - 比如在有`~/.bash_profile`且在`~/.bash_profile`中没有`source ~/.bashrc`时，`bash --login -c`并不会`source ~/.bashrc`，只有`bash -ic`才会
- 是否交互式跑命令，`$0`，`ps`等的输出结果也有区别
  - 在[[zsh]]中提到过
    - 那里想区分`bash`和[[zsh]]，这并不是那么容易
- `bash -i`交互式不能后台运行`&`
  - 前置：[[4-more-commands]]中对多进程的基本了解
  - 比如`bash -ic 'sleep 3; echo 2' & sleep 4; echo 3`
  - 显示`[1]  + 58902 suspended (tty input)  bash -ic 'sleep 3; echo 2'`，然后后台一直suspend不实际运行
  - 所以需要`-i`的，一次只能运行一个
    - 如果你想同时一边运行一边监视和kill，需要让kill的那个进程后台，而`-i`的这个前台
```bash
while [[ 1 -eq 1 ]]
do
    for i in {10..0}
    do 
        echo -e \\033\[34m $i \\033\[0m
        sleep 1
    done
    pid_line=$(ps -ef | grep 'sleep 120' | grep -v grep | grep -v bash)
    if echo $pid_line | grep '[0-9]'
    then
        pid=$(echo $pid_line | awk '{print $3}') # 实则为这一行的ppid
        echo -e \\033\[32m detected $pid \\033\[0m
        echo $pid | xargs kill -9
        break
    fi
done &
bash -ic 'sleep 20; sleep 120'
```