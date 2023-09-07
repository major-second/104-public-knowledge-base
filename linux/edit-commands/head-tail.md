- 常常`| head -n 10 | tail -n 5`
- 由于[[standard-streams]] [[buffer]]机制，往往可以短路求值，从而更快
- 应用
  - 使用了[[cat-tac]] [[find-grep]] [[awk-cut]] [[11-basic-scripting-partB#数学运算基础]] [[off-by-one-errors]]
  - ```bash
    right=$(cat $file | grep -nm 1 pattern | awk -F: '{print $1}')
    left=...
    cat $file | head -n $[$right - 1] | tail -n $[$right - $left] > $output
    ```