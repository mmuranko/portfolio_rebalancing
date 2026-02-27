import yfinance as yf
import pandas as pd

def load_market_data(asset_data):
    df_asset_data = asset_data.copy()

    asset_tickers = df_asset_data['Ticker'].unique().tolist()

    currencies = df_asset_data['Currency'].unique()
    base_currency = 'CHF'
    fx_tickers = []

    for curr in currencies:
        if curr != base_currency: 
            ticker = f"{curr}{base_currency}=X"
            fx_tickers.append(ticker)

    asset_market_data = yf.download(asset_tickers, period="1y")['Close']
    asset_market_data = asset_market_data.ffill().bfill()
    asset_market_data = asset_market_data[asset_tickers]

    fx_market_data = yf.download(fx_tickers, period="1y")['Close']
    
    if isinstance(fx_market_data, pd.Series):
        fx_market_data = fx_market_data.to_frame()

    fx_market_data['CHFCHF=X'] = 1.0
    fx_market_data = fx_market_data.ffill().bfill()
    fx_market_data = fx_market_data[fx_tickers + ['CHFCHF=X']]

    return asset_market_data, fx_market_data