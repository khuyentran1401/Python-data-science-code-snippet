from dotenv import load_dotenv
import os 

load_dotenv()
PASSWORD = os.getenv('PASSWORD')
print(PASSWORD)
# secret_password