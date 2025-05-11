import re
def reverse_letter(st):
    return "".join(re.findall(r"[a-zA-Z]+", st))[::-1]