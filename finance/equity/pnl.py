import numpy as np
import pandas as pd
from time import sleep

def calc_pnl(bid, ask, take_vlm):
    # 1: buy at 22 index: 1
    # -1: sell at 20 index: 0
    length = len(bid)
    bidask = np.vstack((bid, ask))
    row_indices = np.array(take_vlm > 0, dtype=int)
    col_indices = np.arange(length)
    price_per = bidask[row_indices, col_indices]

    delta_cash_sr = -pd.Series(price_per * take_vlm)
    print(delta_cash_sr)
    take_vlm_sr = pd.Series(take_vlm)
    print(take_vlm_sr)
    return delta_cash_sr.cumsum() + take_vlm_sr.cumsum() * bidask.mean(axis=0)

print(calc_pnl(np.array([20, 21, 22, 23, 24, 26]),
            np.array([22, 23, 23, 30, 30, 28]),
            np.array([1, 1, -2, 10, 10, -5])))
sleep(1)