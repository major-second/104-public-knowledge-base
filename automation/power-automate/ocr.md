前置：
- [[power-automate/var]]

内容：
- 常见：`Move to text`，`Wait for text`等
- 注意下方设置可以选择语言。如果是中文必须单独选择
- 如果字太小可能识别不到
  - 可以参考[[misc]]中的快捷键进行放大
- 灰色（对比度太小）的字可能收不到
- 可以选择屏幕一个部分看
  - 应用：一直`Alt+Shift`切换（使用[[control]]中说的无限循环），直到右下角看到指定文字
- 注：这里的Windows OCR Engine性能挺高，相比之下[[tesseract]]就不太行，所以开源的[[my-first-robot]]中，ocr一般不用来“找和点击”，而是用来读取信息，参考[[desktop/basics]]