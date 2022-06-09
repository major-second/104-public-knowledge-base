- [官网](https://digi.bib.uni-mannheim.de/tesseract/)找安装包下载安装
- 安装过程需要联网。需要选择额外装哪些语言（比如你额外选择了Japanese，就会联网下载Japanese数据）
![](download-other-languages.png)
- 安装之后可能需要设定[[windows/env-var]]才能满足一些程序的要求
- 基础命令行用法
  - `tesseract --list-langs`
  - `tesseract <输入路径> <输出路径>`
    - 路径前可以加`-l chi_sim`指定简体中文
    - 输出路径无需加后缀名`.txt`，它会自动加上