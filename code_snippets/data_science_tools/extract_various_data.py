import os 
from datetime import datetime 
import pandas_datareader.data as web 

df = web.DataReader('AD', 'av-daily', start=datetime(2008, 1, 1),
                    end = datetime(2018, 2, 28),
                    api_key=os.getenv('ALPHAVANTAGE_API_KEY'))