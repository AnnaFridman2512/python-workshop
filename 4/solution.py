import re

def main(s):
    # Find sequences of spaces or punctuations
    delimiters = re.findall(r'\s+|[ ,;.]+', s)

    # Split the string based on the found delimiters
    words = re.split(r'\s+|[ ,;.]+', s)

    # Process each word
    processed_words = []
    for word in words:
        if word and word[0].isalpha() and word[0] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            processed_words.append(word.capitalize())
        else:
            processed_words.append(word.lower())

    # Interleave the processed words with the delimiters
    result = []
    for i in range(len(processed_words)):
        result.append(processed_words[i])
        if i < len(delimiters):  # Ensure we don't run out of delimiters
            result.append(delimiters[i])

    # Join everything together
    return ''.join(result)
