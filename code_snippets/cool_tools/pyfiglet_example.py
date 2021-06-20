# pip install pyfiglet
# pip install termcolor

import pyfiglet
from termcolor import colored, cprint

out = pyfiglet.figlet_format("Hello")
print(out)
""" 
    __  __     ____    
   / / / /__  / / /___ 
  / /_/ / _ \/ / / __ \
 / __  /  __/ / / /_/ /
/_/ /_/\___/_/_/\____/ 
"""

out = pyfiglet.figlet_format("Hello", font='slant')
print(out)

cprint(pyfiglet.figlet_format('Hello', font='bell'), 'blue')
""" 
 __  __         .    .         
 |   |    ___   |    |     __. 
 |___|  .'   `  |    |   .'   \
 |   |  |----'  |    |   |    |
 /   /  `.___, /\__ /\__  `._.'
"""