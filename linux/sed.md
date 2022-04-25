`sed`用来做简单的文本编辑
最常见的模式`sed -i '各种命令' 文件名`
- 替换
`sed -i 's/kernel.yama.ptrace_scope = 1/kernel.yama.ptrace_scope = 0/g' /etc/sysctl.d/10-ptrace.conf`
- 插入（第四行前，插入一行`content`）
`sed -i '4i content' file.txt`
    - 含空格`sed -i '4i\ space!' file.txt`
- 插入多行（插入两行`content`）
```sh
sed -i '4i content\
content' file.txt
```

应用：[[zsh]]，[[yama-ptrace-scope]]等