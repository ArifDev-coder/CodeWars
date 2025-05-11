# def find_even_index(arr):
#     for x in range(len(arr)):
#         left = sum(arr[:x])
#         right = sum(arr[x+1:])
        
#         if left == right:
#             return x
        
#     return -1

def find_even_index(arr):
    for x in range(len(arr)):        
        if sum(arr[:x]) == sum(arr[x+1:]):
            return x
        
    return -1


# ! FINALLY!!!!
    
print(find_even_index([1, 2, 3, 4, 3, 2, 1])) # -> 3
print(find_even_index([20,10,-80,10,10,15,35])) # -> 0
print(find_even_index([8, 8])) # -> -1
print(find_even_index([8, 0])) # -> 0
print(find_even_index([0, 8])) # -> 1
print(find_even_index([0, -6, 12, 16, -5, -12, 16, 12, 17, -4, -6, -10, -13, -1, 22, -6, 12, 0, 6, -12, -16])) # -> 5