- https://www.hackerrank.com/challenges/magic-square-forming/problem
  - 三阶幻方一共就8种可能性。可以先定5再定1再讨论8做出论证
  - 得到所有可能幻方，再[[enumerate]]得结果
```python
def formingMagicSquare(s):
    magic_squares = [
        [8,3,4,1,5,9,6,7,2],
        [6,7,2,1,5,9,8,3,4],
        [4,3,8,9,5,1,2,7,6],
        [2,7,6,9,5,1,4,3,8],
        [8,1,6,3,5,7,4,9,2],
        [6,1,8,7,5,3,2,9,4],
        [4,9,2,3,5,7,8,1,6],
        [2,9,4,7,5,3,6,1,8]
    ]
    s = s[0] + s[1] + s[2]
    calc_cost = lambda l: sum(map(lambda x1, x2:abs(x1-x2), l, s))
    return min(map(calc_cost, magic_squares))
```