class DataLoader:

	def __init__(self, data_dir: str):
		self.data_dir = data_dir
		print("Instance is created")

	def __call__(self):
		print("Instance is called")

data_loader = DataLoader('my_data_dir')
# Instance is created

data_loader()
# Instance is called