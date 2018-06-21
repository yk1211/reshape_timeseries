import numpy as np
import pandas as pd
import gc
from multiprocessing import Pool

# csv file 読み込み
# 1千万行ごとの読み込み + GC
df = None

for tmp in  pd.read_csv('eurusd2013.csv', chunksize=10000000):
    if df is None:
        df = tmp
    else:
        df = df.append(tmp, ignore_index=True)
    del tmp
    gc.collect()
    
#　カラム名の変更
df.columns= ['datetime', 'bid', 'ask']

# datetime の型変換
df['datetime'] = pd.to_datetime(df['datetime'])

# indexを変換
df.set_index('datetime', inplace=True)

df = df.resample("5S", how="last")

# NaN行を削除
df = df.dropna()

# csv 出力 - bid
df.to_csv('eurusd2016_bid.csv', columns=['bid'])

# csv 出力 - ask
df.to_csv('eurusd2016_ask.csv', columns=['ask'])
