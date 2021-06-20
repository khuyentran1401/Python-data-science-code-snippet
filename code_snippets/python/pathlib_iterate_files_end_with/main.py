from pathlib import Path 

directory_name = 'data'

# Loop files in a directory
pathlist = Path(directory_name).rglob('*.csv')
for path in pathlist:
    print(str(path))

""" 
data/data3.csv
data/data1.csv
data/data2.csv
"""