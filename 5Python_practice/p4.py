# File reader (files)
with open("notes.txt", "r") as f:
    lines = f.readlines()
line_count = len(lines)
word_count = 0
for line in lines:
    words_in_line = line.split()
    word_count += len(words_in_line)
print(f"Lines: {line_count}")
print(f"Words: {word_count}")
