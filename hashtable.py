import math 
def folding_hash(id, r, table_size): 

    """
    Compute hash using folding method
    """
   
    stringed_id = str(id)
    num_digits = len(stringed_id)
    left_over_digits = num_digits % r
    count = 0 
    temp_str = ""
    sum = 0 
    for i in range(num_digits-left_over_digits):
        temp_str+=stringed_id[i] 
        count +=1
        if(count == r):
            sum+=int(temp_str)
            count = 0
            temp_str = ""
    temp_str=""
    for j in range(left_over_digits):
        temp_str+=stringed_id[num_digits-left_over_digits+j]
    sum+=int(temp_str)
    return sum % table_size


def mid_square_hash(id,r,table_size):
    #r = 2 or r = 3 
    #grab middle of id
    # if r >= string ver of (id) just use the whole id -> base case
    # Example : 10245 with r = 2
    #  want 24  from it so take the middle then alternate right and left  from middle 
    # until r is reached
    #Example : 10245 with r = 3 
    # want 024 -> Take 2 then 4 then 0 
    # return result % table size


#some assert tests

def hashtable_memory_use(relationship_count, hashing_function, r):

    """
    Takes relationship count result from mapreduce, 
    divide into 10 parts,
    and insert them into 10 hashtables using given function and r value, 
    where the hashtables resolve collisions by linked list.
    Returns the memory usage of the resulting hashtables
    """
    list_of_hashtables = [{},{},{},{},{},{},{},{},{},{}]
    entries_per_hashtable = math.ceil(len(relationship_count) / 10)
    count_entries = 0
    count_tables = 0
    for key,val in relationship_count:  


   
        
    

