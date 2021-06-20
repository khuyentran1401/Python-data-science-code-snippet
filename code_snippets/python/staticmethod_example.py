import re 

class ProcessText:
    def __init__(self, text_column: str):
        self.text_column = text_column

    @staticmethod
    def remove_URL(sample: str) -> str:
        """Replace url with empty space"""
        return re.sub(r'http\S+', "", sample)

text = ProcessText.remove_URL('My favorite page is https://www.google.com')
print(text)
# My favorite page is 