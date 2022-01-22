# Inbox

- Here you can write disorganised notes to be categorised later
- Bullet points are useful, but it could be free form text as well
- Sometimes it's better to just get things off your mind quickly, rather than stop to think where it belongs
- But don't let this list get too long
- Move information to more specific documents and link to them.
  - This helps you navigate between documents quickly
  - For example, you can `Cmd`+`Click` this: [[todo]]
- Some notes don't end up making sense the next day
- That's ok, you can just delete them!
  - You can always find them in your git history, if you really need it!


- ubuntu装软件不能同时多个。会报错“锁”啥的自己看
- python3-dev带上pip（依赖！），autoremove会被搞掉

- python typing, np.dtype, namedtuple
  - dtype=namedtuple...: same as `dtype=object`
  - recordtype(要pip装),可以修改
  - np.dtype

-           # todo: in dev for compatibility
            self.history = list(self.history)
            for i in range(len(self.history)):
                item = self.history[i]
                assert isinstance(item, self.HistoryItem)
                self.history[i] = {"frame": item.f_idx, "G": item.G, "state": item.state}
- f2静态行，动态不行！留兼容性！！

- timeshift和挂载的关系（发现没挂载，开timeshift试试）


- 展开函数前外层先重命名`node_outer`等

- `&&` and `; \` are different! `rm -r build && mkdir build && cd build`: bad!