## source
- `source`和直接运行不同
- [参考](https://blog.csdn.net/weixin_44815943/article/details/109353439#:~:text=source%E5%91%BD%E4%BB%A4%201%20%E8%AF%AD%E6%B3%95%EF%BC%9Asource%20filename%20%5Barguments%5D%202%20%E8%BF%94%E5%9B%9E%E5%80%BC%EF%BC%9A%E9%80%80%E5%87%BA%E7%8A%B6%E6%80%81%E7%A0%81,3%20%E5%8F%82%E6%95%B0%EF%BC%9A%E4%BC%A0%E9%80%92%E7%BB%99filename%E7%9A%84%E5%8F%82%E6%95%B0%204%20%E5%8A%9F%E8%83%BD%EF%BC%9Asource%E6%98%AFbash%20shell%E7%9A%84%E5%86%85%E7%BD%AE%E5%91%BD%E4%BB%A4%EF%BC%8C%E7%94%A8%E4%BA%8E%20%E8%AF%BB%E5%8F%96filename%E8%84%9A%E6%9C%AC%E6%96%87%E4%BB%B6%E4%B8%AD%E7%9A%84%E5%91%BD%E4%BB%A4%EF%BC%8C%E5%B9%B6%E5%9C%A8%E5%BD%93%E5%89%8Dshell%E6%89%A7%E8%A1%8C%20%E3%80%82%20%E7%94%B1%E4%BA%8Efilename%E7%9A%84%E6%89%A7%E8%A1%8C%E7%8E%AF%E5%A2%83%E6%98%AF%E5%9C%A8%E5%BD%93%E5%89%8Dshell%EF%BC%8C%E5%9B%A0%E6%AD%A4%E5%B8%B8%E7%94%A8source%E5%91%BD%E4%BB%A4%E5%9C%A8%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6%E6%94%B9%E5%8F%98%E5%90%8E%EF%BC%8C%E9%87%8D%E6%96%B0%E6%89%A7%E8%A1%8C%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6%EF%BC%8C%E9%81%BF%E5%85%8D%E9%87%8D%E6%96%B0%E7%99%BB%E5%BD%95%E3%80%82)
- 在[[shell]]用不了`source`时的[[workaround]]：`eval $(cat my-script.sh)`，是[[meta-programming]]
## 其它
- 作用域：进程！
- `set`可以查询所有，还可以结合[[find-grep]]
## 6.7 数组变量
- [[shell-array]]