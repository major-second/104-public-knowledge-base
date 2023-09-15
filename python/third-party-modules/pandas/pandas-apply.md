例如`df['dtime'] = df['dtime'].apply(lambda x: x.replace(tzinfo=None))`
去除[[timestamps#tzinfo]]