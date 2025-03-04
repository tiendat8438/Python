def remove_int(filename):
    words = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            for word in line.split():
                if word.isdigit():
                    if int(word) > 2**31 - 1:
                        words.append(word)
                else:
                    words.append(word)
    words.sort()
    return " ".join(words)

print(remove_int("DATA.in"))