# Initialize
dvc init

# Track data directory
dvc add data # Create data.dvc
git add data.dvc
git commit -m "add data"

# Store the data remotely
dvc remote add -d remote gdrive://lynNBbT-4J0ida0eKYQqZZbC93juUUUbVH

# Push the data to remote storage
dvc push 

# Get the data
dvc pull 

# Switch between different version
git checkout HEAD^1 data.dvc
dvc checkout
