# pip install graphviz
from graphviz import Graph 

# Instantiate a new Graph object
dot = Graph('Data Science Process', format='png')

# Add nodes
dot.node('A', 'Get Data')
dot.node('B', 'Clean, Prepare, & Manipulate Data')
dot.node('C', 'Train Model')
dot.node('D', 'Test Data')
dot.node('E', 'Improve')

# Connect these nodes
dot.edges(['AB', 'BC', 'CD', 'DE'])

# Save chart
dot.render('data_science_flowchart', view=True)
