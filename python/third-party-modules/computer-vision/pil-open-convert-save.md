- 前置[[pil-image]]
- 命令
    - `open(文件名)`
    - `save(文件名)`
    - `convert('RGB')`
    - `np.array(image)`
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