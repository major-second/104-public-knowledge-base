前置：
- [[dot-robot]]
- 安装[[tesseract]]
  - 并根据`rcc run`的报错提示，额外设置[[windows/env-var]]`PATH`和`TESSDATA_PREFIX`
  - 2022.6：注意新版时`TESSDATA_PREFIX`应该设置到`tessdata`的路径，而不是其上级
  - 这里问题出在RPA的`Desktop`包的提示信息没有及时更新！

参考：
- [[ocr]]
- [[wait-for]]
- [[generalization]]
- [[create-env-yaml]]
- [rpa-desktop文档](https://robocorp.com/docs/libraries/rpa-framework/rpa-desktop)

## 使用`Desktop`包所需前置步骤
- 在`conda.yaml`里增加`rpaframework[cv]`
  - 这个按照官方模板是加在[[pip]]子树，参考[[pip]]和之前的[[dot-robot]]
- 在`tasks.robot`里增加`Library`语句
  - 参考`104-public-knowledge-base\automation\robocorp\example\desktop`中的robot
## 用一次性locators尝试进行基本鼠标操作
- `.robot`中，我们首先学习`Click`和`Wait For Element`命令
  - 很多时候要`Wait For Element`出现了再`Click`
- 参考[rpa-desktop文档](https://robocorp.com/docs/libraries/rpa-framework/rpa-desktop)，综合运用`image:<路径>`，`offset:<x>,<y>`和`ocr:<文本>`等一次性locators，即可完成许多简单任务
  - 参考`104-public-knowledge-base\automation\robocorp\example\desktop\turn-on-wi-fi`中的robot，可自动连接已保存的`eduroam`wifi
    - 这个没有做[[化归]]，是只适用于关闭状态打开wifi并连接指定网络`eduroam`
    - 总之只是个小示例
- [[ocr]]该怎么用
  - ocr找文字进行点击
    - 有时识别率非常低下（文字不够大/字体不理想/对比度不够大时）
      - 使用较新版[[tesseract]]可能好些
    - 只能找在全屏只出现一次的……这点非常不好用
    - 识别速度也不咋地
  - 建议
    - 还是多找图和用[[press-key]]吧
    - ocr在需要读取东西时（先划定区域，再读取这个区域的文字是什么）时才适合用