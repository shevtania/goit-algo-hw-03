import random

def get_numbers_ticket(min, max, quantity):
    seq = set()  #sequence for saving numbers for unique values
    result = [] 
     
    if min < 1 or max > 1000  or (min > max): # verification max and min numbers 
        return result
    
    elif max + 1 - min < quantity:  # numbers must be unique, max - min = quantity - 1
        return result
     
# if upper condition is true, add the integer from the interval (min, max)  in set until the length of the set is  become equal to  quantity.
# After that set is turned into list, and list is sorted
    else:
        while len(seq) < quantity:
            num = random.randrange(min, max + 1)
            seq.add(num)
        
        result = sorted(list(seq))
    return result



