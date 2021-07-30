import numpy as np
import pandas as pd
import texthero as hero

df = pd.DataFrame(
    {
        "text": [
            "Today is a    beautiful day",
            "There are 3 ducks in this pond",
            "This is. very cool.",
            np.nan,
        ]
    }
)

print(df.text.pipe(hero.clean))
"""
0    today beautiful day
1             ducks pond
2                   cool
3                       
Name: text, dtype: object
"""
