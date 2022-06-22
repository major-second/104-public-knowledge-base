用来拼写检查怎么防止它乱报错非英语？
- 确保`"spellright.ducumentTypes"`设置对
- `"spellright.language"`加上你想要的语言（当然这也可以通过`Ctrl+Shift+P`搜索language找到对应命令）
- `.vscode`文件夹中加入workspace特有的`spellright.dict`，放一些词典中原始没收录的单词。
- 不支持中文，别想了