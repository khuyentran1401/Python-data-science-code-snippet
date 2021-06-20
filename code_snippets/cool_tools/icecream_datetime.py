# pip install icecream
from datetime import datetime
from icecream import ic
import time
from datetime import datetime

message = "I don't have prefix"
ic(message)

def time_format():
    return f'{datetime.now()}|> '

ic.configureOutput(prefix=time_format)
for _ in range(3):
    time.sleep(1)
    ic('Hello')

"""
ic| message: "I don't have prefix"
2021-06-20 08:12:21.777664|> 'Hello'
2021-06-20 08:12:22.780577|> 'Hello'
2021-06-20 08:12:23.782396|> 'Hello'
"""