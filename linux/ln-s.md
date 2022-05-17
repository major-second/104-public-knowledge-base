[参考](https://www.cnblogs.com/sueyyyy/p/10985443.html#:~:text=%E8%BD%AF%E8%BF%9E%E6%8E%A5%E6%98%AFlinux%E4%B8%AD%E4%B8%80%E4%B8%AA%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%8C%E5%AE%83%E7%9A%84%E5%8A%9F%E8%83%BD%E6%98%AF%E4%B8%BA%E6%9F%90%E4%B8%80%E4%B8%AA%E6%96%87%E4%BB%B6%E5%9C%A8%E5%8F%A6%E5%A4%96%E4%B8%80%E4%B8%AA%E4%BD%8D%E7%BD%AE%E5%BB%BA%E7%AB%8B%E4%B8%80%E4%B8%AA%E5%90%8C%E4%B8%8D%E7%9A%84%E9%93%BE%E6%8E%A5%E3%80%82%20%E5%85%B7%E4%BD%93%E7%94%A8%E6%B3%95%E6%98%AF%EF%BC%9Aln,-s%20%E6%BA%90%E6%96%87%E4%BB%B6%20%E7%9B%AE%E6%A0%87%E6%96%87%E4%BB%B6%E3%80%82?msclkid=1460c2dacf4711ecb7492bf79d0a5a55)
相当于“快捷方式”。并不真实地“存在”
用法：`ln -s <路径> <文件名或目录>`
查看效果：`ls -l`
- `<路径>`是相对或绝对都有可能
- `<路径>`经常是`<目录>/*`这样的通配符
- `<文件名或目录>`：如果存在目录，就是“到目录下”。否则新建“软链接文件”

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