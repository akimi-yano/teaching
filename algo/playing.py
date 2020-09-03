def ta(b,c):
    return (b+c)

print(ta(1,2) + ta(2,3))



def a():
    b = 100
    print(b)

    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())


def string_substring(string,substring):
    return string.count(substring)

print(string_substring("abcdefgabcab","abc"))