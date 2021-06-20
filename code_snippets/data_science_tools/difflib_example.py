from difflib import SequenceMatcher

text1 = 'I am Khuyen'
text2 = 'I am Khuen'
print(SequenceMatcher(a=text1, b=text2).ratio())
0.9523809523809523