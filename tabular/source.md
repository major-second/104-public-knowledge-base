- 了解`tab`制表符（[[regex]]：`\t`）
Excel选中复制
或者一些网页表格选中复制（比如[这篇文章](https://wires.onlinelibrary.wiley.com/doi/full/10.1002/wcms.1608#:~:text=Generative%20models%20offer%20a%20promising,that%20will%20satisfy%20those%20properties%3F)中的）
直接粘贴成文本，就可能会是用`tab`隔开列，用回车隔开行的结果
- 后处理
  - 可以把`\t`替换成`|`，用于markdown
  - 或可以把`\t`替换成`,`，存储成`.csv`，方便一些软件读取（参考[[file-format]]）