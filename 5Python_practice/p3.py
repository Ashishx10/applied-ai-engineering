# Word counter (dicts)
sentence = "the cat and the dog"
words = sentence.split()
counter = {}
for word in words:
    counter[word] = counter.get(word, 0) + 1
for word, count in counter.items():
    print(f"{word}: {count}")
