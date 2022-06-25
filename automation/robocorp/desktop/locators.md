前置
- [[desktop/basics]]

内容
- 在[[desktop/basics]]中我们学会制造和使用基本的locator，现在了解更多locator相关操作
- 非一次性locator
  - locator具有优良特性：`A locator describes the properties or features of an element. This information can be later used to locate similar elements even when window positions or states change.`，所以非常适合非一次性地使用
  - 具体示例
    - <code>${region}=&nbsp;&nbsp;Find Element&nbsp;&nbsp;ocr:"Customer name"</code>
    - 之后就可以使用`${region}`作为alias
    - 注：`alias:`可以省略，也就是之后可以直接<code>Click&nbsp;&nbsp;${region}</code>
  - 参考`104-public-knowledge-base\automation\robocorp\example\desktop\turn-on-wi-fi-alias`中的robot
- 运算（chaining）
  - `+, |, &, !`四种运算
    - 也可以用`then, not`等单词表示
  - 举例`image:logo.png + offset:600,0 + size:400,200`
  - 举例`!<某图片>`就是某图片不存在