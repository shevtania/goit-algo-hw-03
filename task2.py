import random

def get_numbers_ticket(min, max, quantity):
    seq = set()  
    result = []
     
    if min < 1 or max > 1000  or (min > max): # verification max and min numbers 
        return result
     
# if upper condition is true, add the integer from the intrrval (min, max + 1)  in set until the length of the set is  become equal to  quantity.
# After that set is turned into list, and list is sorted
    else:
        while len(seq) < quantity:
            num = random.randint(min, max + 1)
            seq.add(num)
        
        result = sorted(list(seq))
    return result


