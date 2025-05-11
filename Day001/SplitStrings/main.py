def solution(s):
    if len(s) % 2 != 0:
        s += "_"
    return [s[x:x+2] for x in range(0, len(s), 2)]
        

print(solution("abc"))
