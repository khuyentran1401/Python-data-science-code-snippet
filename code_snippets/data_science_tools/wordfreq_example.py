import matplotlib.pyplot as plt
import seaborn as sns
from wordfreq import word_frequency

print(word_frequency("eat", "en"))  # 0.000135
print(word_frequency("the", "en"))  # 0.0537

sentence = "There is a dog running in a park"
words = sentence.split(" ")
word_frequencies = [word_frequency(word, "en") for word in words]

sns.barplot(words, word_frequencies)
plt.show()
