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
        print("i:",i)
        print("count",count)
        temp_str+=stringed_id[i] 
        count +=1
        if(count == r):
            sum+=int(temp_str)
            count = 0
            temp_str = ""
        print(temp_str)
    temp_str=""
    for j in range(left_over_digits):
        temp_str+=stringed_id[num_digits-left_over_digits+j]
    sum+=int(temp_str)
    return sum % table_size





#some assert tests

def hashtable_memory_use(relationship_count, hashing_function, r):

    """
    Takes relationship count result from mapreduce, 
    divide into 10 parts,
    and insert them into 10 hashtables using given function and r value, 
    where the hashtables resolve collisions by linked list.
    Returns the memory usage of the resulting hashtables
    """

   
        
    

