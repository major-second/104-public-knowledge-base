- `split`
  - 默认使用空白符做split
  - 例如`'ls -lR'.split()`输出`['ls', '-lR']`
    - 这就可用于[[subprocess]]处构造`run`接收的list
  - `'2_3_4'.split('_')`输出`['2', '3', '4']`
  - `'a.b.c.txt'.rsplit('.', 1)`输出`['a.b.c', 'txt']`（从右到左只切一次，用来取[[file-format]]很管用）
- `replace`
  - 比如`s = '1231'; s = s.replace('1', '2'); print(s)`输出`2232`
- `join`把列表中内容变成一个字符串
  - `''.join(list)`就中间没有任何空格，直接紧挨着把内容变成字符串