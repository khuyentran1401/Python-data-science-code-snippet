from pathlib import Path 

file = Path('data')
file.open('w').write('Hello!')

new_p = file.rename(Path("greeting"))

