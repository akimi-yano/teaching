# Write a function that accepts two integers as parameters: size and value. 
# The function should create and return a list whose length is equal to the given size, 
# and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]



# Approach1: initialize an empty array and append the value size times using loop
def approach1(size,value):
    arr = []
    for _ in range(size):
        arr.append(value)
    return arr
print(approach1(4,7))

# Approach2:  list complehension solution in 1 line (basically same thing as the Approach 1 but shorter) 
def approach2(size,value):
    return [value for _ in range(size)]
print(approach2(4,7))

# Approach3: just make [value] and multiply by size (1 line)
def approach3(size,value):
    return [value]*size
print(approach3(4,7))

