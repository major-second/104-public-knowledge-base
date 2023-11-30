- 概述
  - [参考](https://www.cnblogs.com/sueyyyy/p/10985443.html)
  - 相当于“快捷方式”。并不真实地“存在”，也不会真的占物理空间
    - 在[[resource-management/disk]]时很有用
- 用法：`ln -s <路径> <文件名或目录>`
  - 把`<路径>`这个东西搞到`<文件名或目录>`处，这样在后者位置也可以访问前者
    - 注意前提是`<文件名或目录>`中不能有不存在的目录
  - 可以称为`ln -s src dst`
# 查看效果
- `ls -l`，`ll`，`ls -lR`展示
  - `<路径>`是相对或绝对都有可能
  - `<路径>`经常是`<目录>/*`这样的通配符
  - `<文件名或目录>`：如果存在目录，就是“到目录下”。否则新建“软链接文件”
  - 应用：[[linux-cpp-compilers]]，`which c++`然后`ll <路径>`找是否是`g++`
    - oneline: `readlink -f $(which c++)`
- 在文件夹下：`pwd -P`（物理），`pwd -L`（逻辑，使用软连接）

# 相对路径和绝对路径区别
```sh
mkdir 0; \
touch 1; \
ln -s 1 2; \
ls -lR; \
sleep 1; \
mv 2 0; \
ls -lR; \
sleep 1; \
mv 1 0; \
ls -lR; \
sleep 1
```
这时第1，3个`ls -lR`显示`2`有效，第2个显示`2`无效

```sh
mkdir 0; \
touch 1; \
ln -s $(pwd)/1 2; \
ls -lR; \
sleep 1; \
mv 2 0; \
ls -lR; \
sleep 1; \
mv 1 0; \
ls -lR; \
sleep 1
```
这时第1，2个`ls -lR`显示`2`有效，第3个显示`2`无效
而且在`ls -lR`结果中也能看到到底是链接到相对路径还是绝对路径。意义非常明显
拓展：结合本节内容和**如果存在目录，就是“到目录下”的特点**，我们不妨考察：
```sh
mkdir 0; \
touch 1; \
ln -s 1 0; \
ls -lR; \
rm 0/*; \
ln -s $(pwd)/1 0; \
ls -lR
```
的结果。很有意思