# pip install dill

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from dill.source import getname

def save_model(model):
    model_name = getname(model)
    print(f"Saving model as model/{model_name}.pkl")

save_model(KNeighborsClassifier)
save_model(LogisticRegression)

"""Output
Saving model as model/KNeighborsClassifier.pkl
Saving model as model/LogisticRegression.pkl
"""