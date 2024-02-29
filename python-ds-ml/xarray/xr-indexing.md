- 前置，参考：[[xarray]]
# sel-isel
- 类比[[pandas-loc]]和iloc, 这里带有`i`表示index，所以`isel`是通过index（非负整数）选择，`sel`是通过label本身选择
    - `data.isel(lat=0)`
    - `data.isel({"lat": 0})`
# assign
- `.loc[<dict>] = ...`