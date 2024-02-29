- 前置，参考：[[xarray]]
# sel-isel
- 类比[[pandas-loc]]和iloc, 这里带有`i`表示index，所以`isel`是通过index（非负整数）选择，`sel`是通过label本身选择
    - `data.isel(lat=0)`
    - `data.isel({"lat": 0})`
- `drop=True`: 在选择的同时，去掉选择的维度（往往选择的维度需要的label数量是1），类似dataframe到series的转换
    - `data.isel(lat=0, drop=True)`
# assign
- `.loc[<dict>] = ...`