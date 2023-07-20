插件名markdown preview enhanced
可以有[[enhanced]]功能，显示高亮、数学公式等。我们的知识库foam本身[[write-notes-in-foam]]就需要这个插件
- 默认`Ctrl+K V`（这是组合[[keyboard-shortcuts]]）看到预览 
  - 这个不太好用，比如不能在中文环境、只读环境使用。不妨改一下快捷键，参考[[keyboard-shortcuts]]
- 预览右键`Chrome* - PDF`导出[[enhanced]]的pdf，这在写作业导出作业时很好用
    - 但是需要安装[[chrome]]
    - 注意
      - 要先保存才能导出保存后的结果（否则保存结果和预览不同）
      - 如果预览公式正常，导出不正常，可以考虑`.md`文档末尾加入
        ```
        <script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
        <script type="text/x-mathjax-config">
            MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });
        </script>
        ```
        [参考](https://github.com/yzane/vscode-markdown-pdf/issues/21#issuecomment-494048334)
        算是个[[workaround]]