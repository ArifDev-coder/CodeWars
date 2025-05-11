# def open_or_senior(data):
#     result = []
    
#     for x, y in enumerate(data):
#         if data[x][0] >= 55 and data[x][1] >= 7:
#             result.append("Sernior")
#         else:
#             result.append("Open")
#     return result


def open_or_senior(data):
    result = []
    
    for x, y in data:
        if x >= 55 and y >= 7:
            result.append("Senior")
        else:
            result.append("Open")
    return result

print(open_or_senior([[13, 5], [56, 12], [23, 8], [12, 3]]))