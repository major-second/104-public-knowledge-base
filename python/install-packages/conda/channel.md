相当于[[software-management/source]]，就是去哪里下载
- 配置方法参考[[condarc]]
- 应用
  - 换成国内源，提速
  - 对于`pyrosetta`，我们[获得license](https://www.pyrosetta.org/home/licensing-pyrosetta)，然后参考[这个](https://zhuanlan.zhihu.com/p/103840837)，增加`- https://USERNAME:PASSWORD@conda.graylab.jhu.edu` channel，就可以直接`conda install pyrosetta`
    - 有意思的是：channel信息中可以填这些具体的东西