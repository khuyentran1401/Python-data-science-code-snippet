# pip install textblob
import pandas as pd
from textblob import TextBlob

def remove_white_space(df: pd.DataFrame):
    df['text'] = df['text'].apply(lambda row: row.strip())
    return df

def get_sentiment(df: pd.DataFrame):
    df['sentiment'] = df['text'].apply(lambda row:
                                    TextBlob(row).sentiment[0])
    return df

df = pd.DataFrame({'text': ["It is a beautiful day today  ",
                        "  This movie is terrible"]})

df = (df.pipe(remove_white_space)
    .pipe(get_sentiment)
)

print(df)
"""
                          text  sentiment
0  It is a beautiful day today       0.85
1       This movie is terrible      -1.00
"""