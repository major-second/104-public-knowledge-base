- `string = '中文'`
- `b_string = string.encode('utf-8')`
  - `type(b_string)`为`<class 'bytes'>`
    - 它不能用于[[regex]]等操作。可能需要解码`.decode(...)`
    - [[subprocess]]出现过
  - `b_string`为`b'\xe4\xb8\xad\xe6\x96\x87'`，其中`\x`表示十六进制
- `new_string = b_string.decode('gbk')`，得到`'gbk' codec can't decode byte 0xad`，这就是编解码不一致导致中文乱码、无法解码
- 注：`b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')`也可以得到字符串`'中文'`
  - 具体：`b'\xe4\xb8\xad'.decode('utf-8')`就能得到`'中'`
- `string = 'ascii'`当然就没有问题。参考[[ascii]]