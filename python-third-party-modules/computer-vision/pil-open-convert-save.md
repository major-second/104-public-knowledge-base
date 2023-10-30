- 前置[[pil-image]]
- 命令
    - `image = Image.open(<文件名>)`
    - `image.save(<文件名>)`
    - `image.convert(<例: 'RGB'>)`
    - 与[[numpy-basics]]
       - `image_array = np.array(image)`
       - `image = Image.fromarray(<image_array>)`
       - 本质上是一种[[encode-decode]]
       - 注意是否[[normalization#min to max]]过，范围是$[0, 255]$还是$[0,1]$
       - 且如果小数转回整数，需要`.astype(np.uint8)`
- 例子
    ```python
    >>> from PIL import Image
    >>> im = Image.open('<name>.png')
    >>> im
    <PIL.PngImagePlugin.PngImageFile image mode=RGBA size=640x360 at 0x7FCB9CA447B8>
    >>> im.save('foo.jpg') # png有alpha（透明度）通道不能存成jpg
    Traceback (most recent call last):
    (省略若干行)
    OSError: cannot write mode RGBA as JPEG
    >>> im = im.convert('RGB')
    >>> im.save('foo.jpg')
    ```
    可以用来作为基础的可视化方法，帮助看你处理图片的效果