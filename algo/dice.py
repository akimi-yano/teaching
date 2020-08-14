'''
implement a "die" that randomly returns an integer 
between 1 and 6 inclusive. Roll a pair of these 
dice, tracking the statistics until doubles are rolled. 
Display the number of rolls, min, max, and average.  

'''
import random 
def die():
    die1 = float('-inf')
    die2 = float('inf') 
    counter = 0
    max_num = float('-inf')
    min_num = float('inf') 
    total = 0
    while die1 != die2: 
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        counter+=1
        total+=die1+die2
        max_num = max(max_num,die1,die2)
        min_num = min(min_num,die1,die2)
        average = round(total/counter,2)
        print(min_num,max_num,total,counter,average)
    return min_num,max_num,average
print(die())