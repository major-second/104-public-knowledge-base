- 前置
  - [[linux-cpp-compilers]]
  - [参考](https://makefiletutorial.com/)
- > Interpreted languages like Python, Ruby, and raw Javascript don't require an analogue to Makefiles. The goal of Makefiles is to compile whatever files need to be compiled, based on what files have changed. But when files in interpreted languages change, nothing needs to get recompiled. When the program runs, the most recent version of the file is used.
- 其中写的命令和[[shell]]不是一个概念。比如一行一个命令，`cd`结果不持续等等
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