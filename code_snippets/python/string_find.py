sentence = "Today is Saturaday"

# Find the index of first occurrence of the substring
print(sentence.find("day") )
# 2

# Start searching for the substring at index 3
print(sentence.find("day", 3))
# 17

print(sentence.find("nice"))
#-1 
# No substring is found
