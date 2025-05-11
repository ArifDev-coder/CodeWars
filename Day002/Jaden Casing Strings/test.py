# def to_jaden_case(string):
#     x = string.split()
#     words = []
    
#     for i in x:
#         word = i.capitalize()
#         words.append(word)
    
#     print(" ".join(words))
    
def to_jaden_case(string):
    return " ".join(word.capitalize() for word in string.split())



word = "How can mirrors be real if our eyes aren't real, TESTING THIS COEDE"

print(to_jaden_case(word))