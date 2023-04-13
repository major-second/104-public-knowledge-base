from collections import deque
import numpy as np

a = np.array([[0, 9],
[ -5, -10],
[ 9, 9],
[ -6, -9],
[ 7, 3],
[ 4, 3],
[ 4, 3],
[ 1, -3],
[ -2, -4],
[ -6, -5],
[ 4, -2],
[ -2, 0],
[ 2, -3],
[ 2, 3],
[ -2, 7],
[ -6, 8],
[ -5, 6],
[ -4, -6],
[ 2, 8],
[-10, -5],
[-10, -5],
[-10, -5],
[-10, -5],
[-10, -5],
[-10, -5],
[-10, -5],
])
n = 5
o = np.array([[ 0., 0.],
[ -5., -10.],
[ -5., -10.],
[ -6., -10.],
[ -6., -10.],
[ -6., -10.],
[ -6., -9.],
[ -6., -9.],
[ -2., -7.],
[ -8., -12.],
[ -8., -14.],
[ -8., -14.],
[ -8., -11.],
[ -6., -7.],
[ -2., -3.],
[ -8., -3.],
[-13., -3.],
[-17., -6.],
[-17., -6.],
[-15., -6.],
[-20., -10.],
[-30., -15.],
[-40., -20.],
[-50., -25.],
[-50., -25.],
[-50., -25.],
])

def rolling_consecutive_drawdown_brute_force(data, n):
    m, k = data.shape
    ret = np.ndarray((m, k))
    for i in range(m):
        for j in range(k):
            max_drawdown = 0
            curr_drawdown = 0
            for p in range(n):
                curr_idx = i - p
                if curr_idx < 0:
                    break
                curr = data[i-p, j]
                if curr < 0:
                    curr_drawdown += data[i-p, j]
                else:
                    max_drawdown = min(max_drawdown, curr_drawdown)
                    curr_drawdown = 0
            ret[i, j] = min(max_drawdown, curr_drawdown)
    return ret

def rolling_min_considering_truncation(rolling_consecutive_cumsum, consecutive_counter, n):
    ret = rolling_consecutive_cumsum.copy()
    length = len(rolling_consecutive_cumsum)
    my_deque = deque([(rolling_consecutive_cumsum[0], -0)])
    for i in range(1, length):
        if i - n == -my_deque[0][1]:
            my_deque.popleft()
        curr_item = (rolling_consecutive_cumsum[i], -i)
        while my_deque and curr_item < my_deque[-1]:
            my_deque.pop()
        my_deque.append(curr_item)
        ret[i], deque_front_index = my_deque[0][0], -my_deque[0][1]
        if deque_front_index - consecutive_counter[deque_front_index] < i - n:
            ret[i] -= rolling_consecutive_cumsum[i - n]
        if len(my_deque) >= 2:
            ret[i] = min(ret[i], my_deque[1][0])
    return ret

def rolling_consecutive_drawdown(data, n):
    m, k= data.shape
    consecutive_cumsum = np.zeros_like(data)
    consecutive_counter = np.zeros_like(data)
    for i in range(m):
        keep_consecutive = data[i] < 0
        # i=0 is also correct
        consecutive_counter[i] = (consecutive_counter[i-1] + keep_consecutive) * keep_consecutive
        consecutive_cumsum[i] = (consecutive_cumsum[i-1] + data[i]) * keep_consecutive
    
    ret = np.zeros_like(data)
    for i in range(k):
        ret[:, i] = rolling_min_considering_truncation(consecutive_cumsum[:, i], consecutive_counter[:, i], n)
    return ret
'''
The essential part of the analysis is the time complexity of `rolling_min_considering_truncation` function. since it has linear time complexity with respect to m, one gets the overall time complexity of the main function `rolling_consecutive_drawdown` is $O(mk)$.

In fact, there is at most one push and one pop operation performed on the deque for each element. This means that the time complexity of the deque operations is linear with respect to $m$.
'''

assert np.all(np.abs(rolling_consecutive_drawdown_brute_force(a, n) - o) < 1e-3)
assert np.all(np.abs(rolling_consecutive_drawdown(a, n) - o) < 1e-3)