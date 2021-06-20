# pip install num2words
from num2words import num2words

print(num2words(105))
# one hundred and five

print(num2words(105, to='ordinal'))
# one hundred and fifth

print(num2words(105, lang='vi'))
# một trăm lẻ năm

print(num2words(105, lang='es'))
# ciento cinco