import math 
def folding_hash(id, r, ): 

    """
    Compute hash using folding method
    """
    #r = 2 or r = 3
    # take first  r digits then
    # while loop 
    # 10245
    # 102+452+12
    # 012 345 67
    # len 7%3=  2
    stringed_id = str(id)
    num_digits = len(stringed_id)
    left_over_digits = num_digits % r
    count = 0 
    temp_str = ""
    sum = 0 
    for i in range(num_digits-left_over_digits):  #count = 0    # r = 2     temp_str =  24 sum = 10+24  i = 4      num_of_digits = 5 
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
    return sum





#some assert tests

def hashtable_memory_use(relationship_count, hashing_function, r):

    """
    Takes relationship count result from mapreduce, 
    divide into 10 parts,
    and insert them into 10 hashtables using given function and r value, 
    where the hashtables resolve collisions by linked list.
    Returns the memory usage of the resulting hashtables
    """

   
        
    

