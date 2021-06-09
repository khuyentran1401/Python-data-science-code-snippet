from sklearn.datasets import fetch_openml

monk = fetch_openml(name='monks-problems-2', as_frame=True)
print(monk['data'].head(10))
