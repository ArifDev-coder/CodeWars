test = []
strings = "abcd"

# if len(strings) % 2 != 0:
#     strings += "_"
# for x in range(0, len(strings), 2):
#     test.append(strings[x:x+2])

# print("\n\n")
# print(len(strings))

# print(test)

strings += "_"
for x in range(0, len(strings), 2):
    test.append(strings[x:x+2])

print(test)
# ['ab', 'c']

# Result must be ['ab', 'c_']