用来统计文件的基本信息。在[[11-basic-scripting-partA]]有提到
`wc --help`告诉你大概是干啥（`Print newline, word, and byte counts for each FILE`）
可以吃标准输入（`-`为文件），这点和[[find-grep]]类似
作用
- 例如统计`.mp4`视频个数，结合[[find-grep]]
  - `find . -type f -name "*.mp4" | wc`