import re
def find_numbers_1_to_3_digits(string):
    return re.findall(r"\b\d{1,3}\b", string)
def find_specific_words(string, words):
    pattern = r"\b(" + "|".join(words) + r")\b"
    return re.findall(pattern, string)
def find_word_and_position(string, word):
    return [(m.group(), m.start()) for m in re.finditer(rf"\b{word}\b", string)]
def find_substrings(string, substring):
    return [(m.group(), m.start()) for m in re.finditer(re.escape(substring), string)]
def find_occurrences_and_positions(string, substring):
    return [(m.group(), m.start()) for m in re.finditer(re.escape(substring), string)]
def extract_numbers(string):
    return re.findall(r"\d+", string)
def find_words_starting_with_a_or_e(string):
    return re.findall(r"\b[a|e]\w*", string, re.IGNORECASE)
def extract_numbers_with_positions(string):
    return [(m.group(), m.start()) for m in re.finditer(r"\d+", string)]
def find_words_of_length_5(string):
    return re.findall(r"\b\w{5}\b", string)
def find_words_length_1_to_5(string):
    return re.findall(r"\b\w{1,5}\b", string)
def find_words_length_min_5(string):
    return re.findall(r"\b\w{5,}\b", string)
def extract_substrings_in_quotes(string):
    return re.findall(r'"(.*?)"', string)
def find_urls(string):
    return re.findall(r"https?://[^\s]+", string)
def split_by_capital_words(string):
    return re.findall(r"\b[A-Z][a-z]*\b", string)
def is_real_number_with_two_decimals(string):
    return bool(re.fullmatch(r"\d+\.\d{1,2}", string))
