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


def mid_square_hash(id,r):
    #square 
    #r = 2 or r = 3 
    # if r >= string ver of (id) just use the whole id -> base case
    # chck if even or odd
    # when even there will be middle two and grow from there
    # when odd middle one grow from there 
    squared_id = id**2
    print(squared_id)
    string_squared_id= str(squared_id)
    amt_digits = len(string_squared_id)
    if r >= amt_digits:
        return id 
    middle = math.floor(amt_digits/2)
    # default even = middle 2, odd = middle
    half_r = math.floor(r/2)
    print(middle)
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
    print(result)
    




    



    


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
    #for key,val in relationship_count:  


   
        
    

