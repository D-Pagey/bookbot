def get_word_count(content):
    final = []

    words = content.split()

    for word in words:
        if '\n' in word:
            newline = word.split('\n')

            for n in newline:
                final.append(n)
        else:
            final.append(word)

    return len(final)

def count_characters(content):
    counts = {}

    for char in content:
        if char != '\n':
            lowered = char.lower()
            if lowered in counts:
                counts[lowered] += 1
            else:
                counts[lowered] = 1

    return counts

def sort_on(dict):
    return dict["num"]

def sorted_counts(char_dict):
    counts = []

    for k, v in char_dict.items():
        if k.isalpha():
            counts.append({"char": k, "num": v})

    counts.sort(reverse=True, key=sort_on)

    return counts
