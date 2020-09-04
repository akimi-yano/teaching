
def minval(manum):
    if len(manum) == 0:
        return False
    count = manum[0]
    for y in range(0, len(manum), 1):
        if manum[y] < count:
            count = manum[y]
    return count
print(minval([3, 5, -7, 10, -16, 2]))