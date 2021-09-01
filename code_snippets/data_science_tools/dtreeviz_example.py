from dtreeviz.trees import dtreeviz
from sklearn import tree
from sklearn.datasets import load_wine

wine = load_wine()
classifier = tree.DecisionTreeClassifier(max_depth=2)
classifier.fit(wine.data, wine.target)

vis = dtreeviz(
    classifier,
    wine.data,
    wine.target,
    target_name="wine_type",
    feature_names=wine.feature_names,
)

vis.view()
