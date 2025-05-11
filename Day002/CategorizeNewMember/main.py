def open_or_senior(data):
    return ["Senior" if age >= 55 and handicap >= 7 else "Open" for age, handicap in data]
    
print(open_or_senior([[13, 5], [56, 12], [23, 8], [12, 3]]))