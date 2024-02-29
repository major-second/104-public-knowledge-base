- 前置
    - [[pandas]]
    - [[numpy-basics]]
    - [[high-dimension]]
- 联系
  - [[pytorch]]
- https://xarray.dev/
- [基础术语](https://docs.xarray.dev/en/stable/user-guide/terminology.html#term-Broadcasting)
-   ```python
    """
    To try Xarray in the browser,
    use the console located 👉 or 👇:
    1. Type code in the input cell and press
    Shift + Enter to execute
    2. Or copy paste the code, and click on
    the "Run" ▶ button in the toolbar
    """
    import xarray as xr
    import pandas as pd
    import numpy as np

    data = xr.DataArray(
        np.random.randn(3, 2, 3),
        dims=("time", "lat", "lon"),
        coords={
            "lat": [10, 20],
            "time": pd.date_range(
                "2020-01", periods=3, freq="MS"
            ),
        },
    )

    # positional and by integer label, like numpy
    data[0, :]

    # loc or "location": positional and
    # coordinate label, like pandas
    data.loc[:, 10]

    # isel or "integer select": by dimension name
    # and integer label
    data.isel(lat=0)

    # sel or "select": by dimension name and
    # coordinate label
    data.sel(time="2020-01")

    # Data aggregations uses dimension names
    # instead of axis numbers
    data.mean(dim=["time", "lat"])

    # quick and convenient visualizations
    data.isel(lon=0).plot();

    # Pretty neat, eh? :)
    # For more, head over to the documentation page
    ```