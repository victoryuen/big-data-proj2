from functools import reduce
from data_extraction import *

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

    #map data
    mapped_data = reduce(lambda x, y: x + y, map(mapper, dict_compound_bind_gene.items()))
    #reduce 
    compound_counts = reduce(reducer, mapped_data, {})
    print(compound_counts.get("Compound::DB01268"))
    print(max(compound_counts, key=compound_counts.get))
    
if __name__ == "__main__":
    main()


