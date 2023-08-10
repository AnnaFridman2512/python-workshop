import re

def main(sentence):
    words = re.split(r'[ ,.;:\'"(){}]+', sentence)  # Split the sentence using regular expression
    longest_word = max(words, key=len)  # Find the longest word based on length
    return longest_word