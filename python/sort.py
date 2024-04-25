sentence = input("Enter a sentence: ")
words = [word.lower() for word in sentence.split()]
words.sort()
for word in words:
    print(word)
