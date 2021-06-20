from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC 
from sklearn.datasets import load_iris 

# load data
df = load_iris()
X = df.data
y = df.target 

# split data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# Create a pipeline variable
make_pipe = make_pipeline(StandardScaler(), SVC())

# Defining parameters grid
grid_params = {'svc__C': [0.1, 1, 10, 100, 1000], 'svc__gamma': [0.1, 1, 10, 100]}

# hypertuning
grid = GridSearchCV(make_pipe, grid_params, cv = 5)
grid.fit(X_train, y_train)

# predict
y_pref = grid.predict(X_test)