words = input("Enter a list of words separated by space: ").split()
words.sort()
print("Words in alphabetical order: ")
for word in words:
    print(word)