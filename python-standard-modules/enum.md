```python
import enum
class Color(enum.Enum):
    RED = 1 # or: RED = 'red'
    GREEN = 2
    BLUE = 3
print(Color.RED)
print(Color.RED.value)
```
- [[naming#有名字作为交流基础]]，防止手输字符串等
- [[naming-in-coding]]