前置[[oi-wiki-basic/var]]

https://oiwiki.org/lang/branch/
# `if`
`if(){}`
`if(){}else{}`
`if(){}else if(){}else{}`
# `switch`
```cpp
switch(整型){
    case 1:
     ...;
     break;
    default:
     ...;
}
```
`switch`的书写逻辑上和`if`不太一样：花括号加到“总体”，表示这些标签“从属于”`switch`语句
- 当然，内部也可以加花括号。并且需要定义变量时，必须加花括号
- 注意`break`
  - 所以说除非你确保控制流程简单明了，否则就别用`switch`了。到时候中间又有`break`你就尴尬了