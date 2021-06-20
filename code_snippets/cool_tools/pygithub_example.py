from github import Github 

# g = Github('user', 'password') # use username and password
g = Github('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') # or use an access token

for i, repo in enumerate(g.search_topics('machine learning')):
    if i < 10:
        print(repo.name)

"""
machine-learning
deep-learning
scikit-learn
jupyter-notebook
scikitlearn-machine-learning
coursera
unsupervised-machine-learning
supervised-machine-learning
coursera-machine-learning
adversarial-machine-learning
"""