import re
def remove_leading_zeros(ip):
    return re.sub(r"\b0+(\d)", r"\1", ip)
def replace_spaces_with_underscores(string):
    return string.replace(" ", "_")
def replace_underscores_with_spaces(string):
    return string.replace("_", " ")
def extract_date_from_url(url):
    return re.findall(r"(\d{4})-(\d{2})-(\d{2})", url)
def convert_date_format(date):
    return re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3-\2-\1", date)
def extract_numbers(string):
    return re.findall(r"\d+", string)
def shorten_road(string):
    return re.sub(r"\bRoad\b", "Rd.", string)
def remove_whitespace_and_punctuation(string):
    return re.sub(r"[ ,.:]+", "", string)
def replace_two_occurrences(string):
    return re.sub(r"[ ,.:]{1,2}", " ", string)
def camel_to_snake(string):
    return re.sub(r"(?<!^)(?=[A-Z])", "_", string).lower()
def snake_to_camel(string):
    return re.sub(r"_([a-z])", lambda x: x.group(1).upper(), string)
def replace_multiple_spaces(string):
    return re.sub(r"\s+", " ", string)
def remove_whitespace(string):
    return re.sub(r"\s+", "", string)
def remove_non_alphanumeric(string):
    return re.sub(r"[^a-zA-Z0-9]", "", string)
def find_urls(string):
    return re.findall(r"https?://[^\s]+", string)
def replace_ignore_case(string, old, new):
    return re.sub(re.escape(old), new, string, flags=re.IGNORECASE)
def split_with_multiple_separators(string):
    return re.split(r"[ ,;|]+", string)
def remove_short_words(string, length):
    return re.sub(rf"\b\w{{1,{length}}}\b", "", string).strip()
