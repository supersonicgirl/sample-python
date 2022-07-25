import ccxt
import schedule
import time
import pandas as pd
import config
from ta.utils import _ema
import requests

def sendSignal(SIGNAL_MESSAGE):
    base_url = 'https://api.telegram.org/bot5574070283:AAEwwDxoG6dCtSKgO7E59ZCxXymhgB9Tx2o/sendMessage?chat_id=-722668052&text={}'.format(SIGNAL_MESSAGE)
    requests.get(base_url) 

def TillsonT3():
    TIME_RANGE = '15m'
    exchange = ccxt.binance ({
        'apiKey': config.BINANCE_API_KEY,
        'secret': config.BINANCE_SECRET_KEY
    })
    
    
    
    markets = exchange.load_markets()

    bars = exchange.fetch_ohlcv('BTC/USDT', TIME_RANGE, limit=45)
    df = pd.DataFrame(bars, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    
    length1 = 8
    a1 = 0.7
    df['e1'] = _ema((df['high'] + df['low'] + 2 * df['close']) / 4, length1)
    df['e2'] = _ema(df['e1'], length1)
    df['e3'] = _ema(df['e2'], length1)
    df['e4'] = _ema(df['e3'], length1)
    df['e5'] = _ema(df['e4'], length1)
    df['e6'] = _ema(df['e5'], length1)

    df['c1'] = -a1 * a1 * a1
    df['c2'] = 3 * a1 * a1 + 3 * a1 * a1 * a1
    df['c3'] = -6 * a1 * a1 - 3 * a1 - 3 * a1 * a1 * a1
    df['c4'] = 1 + 3 * a1 + a1 * a1 * a1 + 3 * a1 * a1

    df['T3'] = df['c1'] * df['e6'] + df['c2'] * df['e5'] + df['c3'] * df['e4'] + df['c4'] * df['e3']

    df['T3Diff'] = df['T3'].diff()

    SIGNAL_MESSAGE = 'AAA'
    print(SIGNAL_MESSAGE)
    sendSignal(SIGNAL_MESSAGE) 

    if (df['T3Diff'][df.index[-2]] < 0 and df['T3Diff'][df.index[-1]] > 0):
        SIGNAL_MESSAGE = 'T3 BUY SIGNAL in '+ TIME_RANGE + ' for BTC price '+ "${:,.0f}".format(df['close'][df.index[-1]])
        sendSignal(SIGNAL_MESSAGE) 
        print(SIGNAL_MESSAGE)

    elif (df['T3Diff'][df.index[-2]] > 0 and df['T3Diff'][df.index[-1]] < 0):
        SIGNAL_MESSAGE = 'T3 SELL SIGNAL in '+ TIME_RANGE + ' for BTC price '+ "${:,.0f}".format(df['close'][df.index[-1]])
        sendSignal(SIGNAL_MESSAGE)
        print(SIGNAL_MESSAGE)
        

def main():
      schedule.every(3).seconds.do(TillsonT3)
      #schedule.every(15).minutes.do(TillsonT3)

      while 1:
            schedule.run_pending()
            time.sleep(1)

if __name__ == '__main__':
      main()
         


   




