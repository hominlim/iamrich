import mojito
import pprint

f = open("./mock.key")
lines = f.readlines()
key = lines[0].strip()
secret = lines[1].strip()
acc_no = lines[2].strip()
f.close()

broker = mojito.KoreaInvestment(
    api_key=key,
    api_secret=secret,
    acc_no=acc_no
)

resp = broker.fetch_price("005930")
pprint.pprint(resp)