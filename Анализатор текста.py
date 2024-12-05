text = input("Введите текст: ")
text = text.lower()

punctuation = [".", ",", "!", "?"]

for char in punctuation:
    text = text.replace(char, "")

words = text.split()

a = set(words)
b = len(a)

word_frequency = {}
for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    elif word not in word_frequency:
        word_frequency[word] = 1

print("Количество разных слов:", b)
print("Частота слов:")
for word, frequency in word_frequency.items():
    print(f"{word}: {frequency}")