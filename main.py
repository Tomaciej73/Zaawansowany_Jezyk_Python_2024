import re
def contains_only_alphanum(string):
    return bool(re.fullmatch(r"[a-zA-Z0-9]*", string))
def starts_with_a_and_b(string):
    return bool(re.match(r"a[b]*", string))
def starts_with_a_and_one_b(string):
    return bool(re.match(r"a.*b", string))
def starts_with_a_and_three_b(string):
    return bool(re.match(r"a[^b]*b[^b]*b[^b]*b[^b]*", string))
def starts_with_a_and_two_to_three_b(string):
    return bool(re.match(r"a([^b]*b){2,3}[^b]*", string))
def find_small_letters_with_underscore(string):
    return re.findall(r"[a-z]+_[a-z]+", string)
def find_capital_and_lowercase(string):
    return re.findall(r"[A-Z][a-z]*", string)
def starts_with_a_ends_with_b(string):
    return bool(re.match(r"a.*b$", string))
def word_at_start(string):
    return bool(re.match(r"^\w+", string))
def word_at_end_with_punctuation(string):
    return bool(re.search(r"\w+[.,!?]?$", string))
def words_with_z(string):
    return re.findall(r"\b\w*z\w*\b", string)
def words_with_z_not_start_or_end(string):
    return re.findall(r"\b\w+z\w+\b", string)
def find_mixed_substrings(string):
    return re.findall(r"[a-zA-Z0-9_]+", string)
def starts_with_digit(string):
    return bool(re.match(r"^\d", string))
def ends_with_digit(string):
    return bool(re.search(r"\d$", string))
