# Befort isort
from sklearn.metrics import confusion_matrix, fl_score, classification_report, roc_curve
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn import svm
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import TimeSeriesSplit

# On your terminal: isort name_of_your_file.py 
from sklearn import svm
from sklearn.metrics import (classification_report, confusion_matrix, fl_score,
                             roc_curve)
from sklearn.model_selection import (GridSearchCV, StratifiedKFold,
                                     TimeSeriesSplit, train_test_split)
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
