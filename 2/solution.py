def main(str):

    reversed_words = []
    words = str.split()

    for word in words:
        reversed_word = ''.join(reversed(word))
        reversed_words.append(reversed_word)

    reversed_words.reverse()  # Reverse the list of reversed words

    return ' '.join(reversed_words)