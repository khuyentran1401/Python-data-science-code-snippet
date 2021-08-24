import pandas as pd

df = pd.DataFrame(
    {
        "item": ["apple", "apple", "apple", "apple", "apple"],
        "size": ["small", "small", "large", "large", "large"],
        "location": ["Walmart", "Aldi", "Walmart", "Aldi", "Aldi"],
        "price": [3, 2, 4, 3, 2.5],
    }
)

print(df)

pivot = pd.pivot_table(
    df, values="price", index=["item", "size"], columns=["location"], aggfunc="mean"
)
print(pivot)
