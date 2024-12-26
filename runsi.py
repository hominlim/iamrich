import mojito
import pprint
import pandas as pd

f = open("./mocke.key")
lines = f.readlines()
key = lines[0].strip()
secret = lines[1].strip()
acc_no = lines[2].strip()
f.close()

broker = mojito.KoreaInvestment(
    api_key=key,
    api_secret=secret,
    acc_no=acc_no,
    mock=True
)

data=[]
resp = broker.fetch_ohlcv(symbol="005930", timeframe='D', adj_price=True)
# pprint.pprint(resp)

df = pd.DataFrame(resp['output2'])
dt = pd.to_datetime(df['stck_bsop_date'], format="%Y%m%d")
df.set_index(dt, inplace=True)
df = df[['stck_oprc', 'stck_hgpr', 'stck_lwpr', 'stck_clpr']]
df.columns = ['open', 'high', 'low', 'close']
df.index.name = "date"
print(df)