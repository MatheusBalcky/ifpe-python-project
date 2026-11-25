import pandas as pd
import yfinance as yf

def download_data(ticker:str) -> pd.DataFrame:
    """
    Download historical data.
    
    Args:
        ticker (str): Ticker name

    """
    data = yf.download(ticker, multi_level_index=False).reset_index()
    
    return data