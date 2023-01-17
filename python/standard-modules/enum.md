```python
import enum
class Color(enum.Enum):
    RED = 1 # or: RED = 'red'
    GREEN = 2
    BLUE = 3
print(Color.RED)
print(Color.RED.value)
```