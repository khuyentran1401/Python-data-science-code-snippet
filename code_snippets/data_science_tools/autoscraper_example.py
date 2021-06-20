# pip install autoscraper

from autoscraper import AutoScraper

url = 'https://stackoverflow.com/questions/2081586/web-scraping-with-python'

wanted_list = ['How to check version of python modules?']

scraper = AutoScraper()
result = scraper.build(url, wanted_list)

for res in result:
    print(res)
""" 
How to execute a program or call a system command from Python
What are metaclasses in Python?
Does Python have a ternary conditional operator?
Convert bytes to a string
Does Python have a string 'contains' substring method?
How to check version of python modules?
"""