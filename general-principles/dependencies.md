- 位置依赖
    - 很多软件不能随便挪位置（但是`portable`标记的当然就可以）
- 版本依赖
    - 参考[[upgrade]]. 一般来说，很多依赖都是要求`>=`某某版本，而且上层版本越高，需求的底层版本也越高。所以在两头确定时，中间可行的版本可能就只有一个范围。不能太高也不能太低
    - 有些时候，兼容性比较差，就要求底层必须是某某版本范围，不是`>=`都行。比如cuda10和11这种