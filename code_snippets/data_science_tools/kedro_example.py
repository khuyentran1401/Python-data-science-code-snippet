from kedro.pipeline import node, Pipeline
from kedro.io import DataCatalog, MemoryDataSet
from kedro.runner import SequentialRunner

# Prepare a data catalog
data_catalog = DataCatalog({"data.csv": MemoryDataSet()})

# Prepare first node
def process_data():
    return f"processed data"

process_data_node = node(
    func=process_data, inputs=None, outputs="processed_data"
)

def train_model(data: str):
    return f"Training model using {data}"

train_model_node = node(
    func=train_model, inputs="processed_data", outputs="trained_model"
)

# Assemble nodes into a pipeline
pipeline = Pipeline([process_data_node, train_model_node])

# Create a runner to run the pipeline
runner = SequentialRunner()
print(runner.run(pipeline, data_catalog))
# {'trained_model': 'Training model using processed data'}