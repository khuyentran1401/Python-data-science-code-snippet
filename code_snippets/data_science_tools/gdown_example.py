# pip install gdown
import gdown

# Format of url: https://drive.google.com/uc?id=YOURFILEID
url = 'https://drive.google.com/uc?id=1jI1cmxqnwsmC-vbl8dNY6b4aNBtBbKy3'
output = 'Twitter.zip'

gdown.download(url, output, quiet=False)
