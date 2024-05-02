from functools import reduce
from data_extraction import *
from mapreduce import *

def mapper(compound_binds):
    compound, binds = compound_binds
    return [(compound, 1) for _ in binds]
def reducer(counts, pair):
    compound, bind_count = pair
    counts[compound] = counts.get(compound, 0) + bind_count
    return counts

def main():
    # Part 1
    dict_compound_bind_gene = get_relationships("Compound", "CbG")
    dict_disease_upregulate_gene = get_relationships("Disease", "DuG")

    # Part 2
    # map data
    mapped_data = reduce(lambda x, y: x + y, map(mapper, dict_compound_bind_gene.items()))

    # reduce 
    compound_counts = reduce(reducer, mapped_data, {})

    #Top 5 
    #print(compound_counts.items())
    top_compounds = sorted(compound_counts.items(), key= lambda x: x[1],reverse=True)
    print("The top 5 compounds are ", top_compounds[:5])

    # Part 3

    
if __name__ == "__main__":
    main()


