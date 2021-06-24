from pathlib import Path 

file = 'test1/test2/test.txt'
print(Path(file).parents[0])
print(Path(file).parents[1])
print(Path(file).parents[2])
print(Path(file).parents[2].resolve())
