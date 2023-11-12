- 前置
  - [[shell-expansion]]
- [参考](https://www.gnu.org/software/bash/manual/html_node/Filename-Expansion.html)
- 在[[shell-quotes]] removal之前，所以`"*"`不会被expand
- 和[[regex]]显然不同，比如`*`相当于[[regex]]的`.*`
- 但`[1-3]`这种仍然能用
- 拓展：Brace Expansion: `echo a{b,c,d}e`