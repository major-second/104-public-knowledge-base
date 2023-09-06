- `:`参考对比[[awk-cut]], [[slice]]
- [参考](https://www.gnu.org/software/bash/manual/html_node/Shell-Parameter-Expansion.html)
- ```bash
  var=123456
  echo $var
  echo ${var:0:1}
  echo ${var:1:2} # 2 chars, not [left, right) or so
  echo ${var:1:3}
  echo ${var:3}
  echo ${var:0-3}
  echo ${var:0-3:2}

  var=1a2a3a4
  echo ${var/a/}
  echo ${var//a/}
  echo ${var#1a}
  echo ${var#*a}
  echo ${var##*a}
  echo ${var%a*}
  echo ${var%%a*}
  ```
- 输出
  ```
  123456
  1
  23
  234
  456
  456
  45
  12a3a4
  1234
  2a3a4
  2a3a4
  4
  1a2a3
  1
  ```