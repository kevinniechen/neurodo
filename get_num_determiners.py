import re

def get_num_determiners(text):
    deter = ["that", "what", "whatever", "which", "whichever"]
    count = 0

    for word in deter:
        count += sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word), text))

    return count
