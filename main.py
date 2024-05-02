from data_extraction import *
from mapreduce import *
from hashtable import *

def main():
    # Part 1

    dict_compound_bind_gene = get_relationships("Compound", "CbG")
    dict_disease_upregulate_gene = get_relationships("Disease", "DuG")

    # testing code
    # print(dict_compound_bind_gene)
    # print(dict_disease_upregulate_gene)

    print("--------- Part 2 ---------\n")

    compound_bind_gene_count = mapreduce(dict_compound_bind_gene)
    top_compounds = sorted(compound_bind_gene_count.items(), key = lambda x: x[1], reverse=True)
    print("Top 5 compounds based on bindings with genes:")
    for compound in top_compounds[:5]:
        print(compound[0], compound[1]) # TODO: data_extraction.py: a function for id --> name

    print("\n--------- Part 3 ---------\n")

    disease_upregulate_gene_count = mapreduce(dict_disease_upregulate_gene)
    top_diseases = sorted(disease_upregulate_gene_count.items(), key = lambda x: x[1], reverse=True)
    print("Top 5 disease based on upregulation with genes:")
    for disease in top_diseases[:5]:
        print(disease[0], disease[1]) # TODO: data_extraction.py: a function for id --> name

    print("\n---------- Part 5a ----------\n")

    # something like this
    # r_3 = hashtable_memory_use(compound_bind_gene_count, folding_hash, 3)
    # r_4 = hashtable_memory_use(compound_bind_gene_count, folding_hash, 4)

    # print(((r_3 < r_4) ? "r = 3" : "r = 4"), "uses the least storage")

    print("\n---------- Part 5b ----------\n")

    # something like this
    # r_3 = hashtable_memory_use(disease_upregulate_gene_count, folding_hash, 3)
    # r_4 = hashtable_memory_use(disease_upregulate_gene_count, folding_hash, 4)

    # print(((r_3 < r_4) ? "r = 3" : "r = 4"), "uses the least storage")


    
if __name__ == "__main__":
    main()


