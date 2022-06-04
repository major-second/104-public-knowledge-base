前置：
- [[open-convert-save]]

- `from torchvision import transforms as tfs`
- `tfs.大写开头类名(参数)`可以得到实际用来transform的函数
- 原图![](original.png)，参考[[open-convert-save]]`open`到`ori`
    - 零元`h_flip = tfs.RandomHorizontalFlip()(ori)`
      - ![](h-flip.png)
      - 效果随机（之后有的也是）。不一定是这样
    - 一元`random_cropped = tfs.RandomCrop(100)(ori)`
      - ![](random-crop.png)
    - `center = tfs.CenterCrop(100)(ori)`
      - ![](center-crop.png)
    - `rotated = tfs.RandomRotation(30)(ori)`
      - ![](rotate.png)
    - 一或二元`resized = tfs.Resize((800, 1000))(ori)`
      - ![](resize.png)
      - 注：crop和resize常常配套使得大小确定！
    - 一至四元均可`jittered = tfs.ColorJitter(contrast=0.5, brightness=0.5, hue=0.5)(ori)`
      - ![](color-jitter.png)