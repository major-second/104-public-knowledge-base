- 参考
  - [[pricing]]
  - [[temp-solution]]
  - [[region-language]]
  - [[vpn]], [[proxy-basics]], [[configure-proxy]]
  - [[sms]]
- 有些地方特定身份（一般指ip）才能上/使用/发消息等等
  - 参考[[proxy-basics]]的是否全局[[configure-proxy]], [[vpn]]
  - 例子[[chatgpt]], [[telegram]], [[new-bing]]
  - [[spotify]]定期挂代理上个线确认，等
- 邀请码
  - 可能可以获得优惠，例如[[binance]]
    - 优惠可以分成，比如你分多点，或者受邀请人分多点
  - 可能有邀请码才能进，比如[[nobepay]]
- 验证：邮箱、手机、2FA等
  - 一般国外邮箱比国内好
    - 一个折中[[workaround]]：[[outlook]]
    - 最好：[[google]]，一般都没问题，但是需要能翻墙
  - 邮箱、手机注意看垃圾邮件、骚扰短信文件夹！否则可能漏
  - 手机：有时需要[[sms]]
  - 地址（如[[apple-id]]美区需要）
    - 例如 https://www.meiguodizhi.com/
    - 生成的可能邮编不对，等等，需要自己手动修改一下
    - 注意查美国免税区
    1. 俄勒冈州（Oregon）
    2. 阿拉斯加州（Alaska）
    3. 特拉华州（Delaware）
    4. 蒙大拿州（Montana）
    5. 新罕布什尔州（New Hampshire）
# 2FA
- 比如Google, Microsoft等都有相关产品。根据公司，app（例如[[binance]]）需要可能需要不同的authenticator
- 相当于用手机提供第二重验证，有动态口令等功能。可以借用手机上的人脸识别、指纹等
- 换手机前，需要妥善处理这个，否则可能造成不便
  - 关联的东西是手机上层软件、数据，比物理的电话卡、在线的email要脆弱得多！

# 登录方式
- 账号密码
- 邮箱验证码
- 手机验证码
- 有些时候可以直接用第三方账号如[[google]]登录
  - 举例[[spotify]]
    - [[google]]可以做[[temp-solution]]，先成功注册登录
    - 之后可以设置普通密码，变成邮箱+密码登录
      - 而非只能用[[google]]登录
- 找回密码：往往需要邮箱手机等
  - 所以如果怕密码忘记，注册时就要相应绑定
  - 更改密码时可能会登出其它地方所有登录
- [[web-api]]
  - 自动化时用
  - 举例
    - [[binance-api]]
    - [[openai-api]]
  - 常常也有“账号密码”一说
  - 特别小心不要[[push-pull#push]]到[[github]]上了……
## passkey
- 例如 FaceID, 指纹等 biometrics
- 往往可替代[[account#2FA]]或者手机邮箱验证码等麻烦的
# 定期活跃
  - 一些账户不定期登录可能会被删除、降级等
    - [[telegram]]
    - [[net-disk]]中的部分，比如[[mega]]
  - 还有些[[spotify]]需要定期验证你的地址等