- 前置
  - [[linux-cpp-compilers]]
  - [参考](https://makefiletutorial.com/)
  - [参考](https://www.zhaixue.cc/makefile/makefile-intro.html)
- > Interpreted languages like Python, Ruby, and raw Javascript don't require an analogue to Makefiles. The goal of Makefiles is to compile whatever files need to be compiled, based on what files have changed. But when files in interpreted languages change, nothing needs to get recompiled. When the program runs, the most recent version of the file is used.
- 其中写的命令和[[shell]]不是一个概念
  - 比如一行一个命令，`cd`结果不持续
    - 需要前面加`.ONESHELL:`才是一个整体
  - 中途出现返回值非零被视为失败
  - 有一些转义等和裸[[shell]]不同，比如`$${KEY}`相当于[[shell]]的`${KEY}`，`@echo ...`防止输出两遍，等等
- 基本模式
  ```makefile
  all: one two three

  one:
  	touch one
  two:
  	touch two
  three:
  	touch three

  .PHONY: clean
  clean:
  	rm -f one two three
  ```
  - `make`等于`make all`
  - `make clean`就是[[refresh]]
    - [[phony]]
- 注意
  - 更新了东西就会导致后续依赖 outdated （日期更老），后面都需要重新make
    - 毕竟make原始的逻辑就是处理编译型语言的依赖
  - 相反，如果一个命令不更新文件，那么make就会认为它没有执行成功（没有产生最新版文件）
    - 例如[[poetry-lock]]，`poetry lock`，如果不是删除`poetry.lock`重新生成，即使更新了`poetry.lock`，`ll`时看时间也可能不变，就不会被make认为成功生成（新）目标
      - 这种情况来源是 `/etc/fstab`中的某些参数
    - 例如：一个target的代码块完全不产生文件，将会导致每次`make`都会被运行
      - [参考](https://stackoverflow.com/questions/47932338/gnu-make-always-considers-a-non-file-target-as-being-remade-possible-bug)
    - [[phony]]的作用就是即使实际产生了文件，也总是当作没有产生，每次都运行