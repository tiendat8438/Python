from collections import Counter

def isPalin(s):
    return s == s[::-1]

def is_valid_word(s):
    return ''.join(c for c in s if c.isalnum())

def find_longest_palin_string(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        words = [is_valid_word(word).upper() for word in f.read().split()]

    words = [word for word in words if word]
    palin_words = [word for word in words if isPalin(word)]
    if not palin_words:
        return
    word_counts = Counter(palin_words)
    max_len = max(len(word) for word in palin_words)
    seen = set()
    longest_palins = [(word, word_counts[word]) for word in words if word in word_counts and len(word) == max_len and word not in seen and not seen.add(word)]
    for word, count in longest_palins:
        print(word, count)

find_longest_palin_string("VANBAN.in")