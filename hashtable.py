import sys
import math
from functools import reduce

def folding_hash(id, r, table_size): 
    """
    Compute hash using folding method
    """
    num_digits = len(id)
    left_over_digits = num_digits % r
    count = 0 
    temp_str = ""
    sum = 0 

    for i in range(num_digits - left_over_digits):
        temp_str += id[i] 
        count += 1

        # reached one "segment" of r length
        if(count == r):
            sum += int(temp_str)
            count = 0
            temp_str = ""

    temp_str = ""
    if(left_over_digits > 0): # remaining digits less than r length
        for j in range(left_over_digits):
            temp_str += id[num_digits - left_over_digits + j]
        sum += int(temp_str)
        
    return sum % table_size

def mid_square_hash(id,r,table_size):
    #square 
    #r = 2 or r = 3 
    # if r >= string ver of (id) just use the whole id -> base case
    # chck if even or odd
    # when even there will be middle two and grow from there
    # when odd middle one grow from there 
    squared_id = id**2
    string_squared_id= str(squared_id)
    amt_digits = len(string_squared_id)
    if r >= amt_digits:
        return id 
    middle = math.floor(amt_digits/2)
    # default even = middle 2, odd = middle
    half_r = math.floor(r/2)
    if(amt_digits%2 == 0):
        if(r%2 == 0):
            result = string_squared_id[middle-half_r:middle+half_r]
        else:
            result = string_squared_id[middle-half_r :middle+half_r +1]
    else:
        if(r%2 == 0):
            result = string_squared_id[middle-half_r+1:middle+half_r+1]
        else:
            result = string_squared_id[middle-half_r :middle+half_r+1]
    return result % table_size


def hashtable_memory_use(relationship_count, hash_function, r):
    """
    Takes relationship count result from mapreduce, 
    divide into 10 parts,
    and insert them into 10 hashtables using given function and r value, 
    where the hashtables resolve collisions by linked list.
    Returns the memory usage of the resulting hashtables
    """
    list_of_hashtables = [{},{},{},{},{},{},{},{},{},{}]
    entries_per_hashtable = round(len(relationship_count) / 10)

    count_entries = 0
    count_tables = 0

    for key, val in relationship_count.items():  
        # get id
        if (key[0:7] == "Disease"):
            id  = key.split(":")[3] # splits Disease::DOID:0050156 example to  "Disease"," ","DOID","0050156"
        elif (key[0:8] == "Compound"):
            id = key.split("DB")[1]

        # populate which table
        if (count_entries == entries_per_hashtable and count_tables != 9):
            count_tables += 1
            count_entries = 0

        # insertions
        index = hash_function(id, r, entries_per_hashtable)
        table = list_of_hashtables[count_tables]
        
        if index in table:
            table[index].append((key, val))
        else:
            table[index] = [(key, val)]

        count_entries += 1
            
    return reduce(lambda sum, table: sum + sys.getsizeof(table), list_of_hashtables, 0)