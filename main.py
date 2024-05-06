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
        name_compound = id_to_name(compound[0],nodes_df)
        print(name_compound, compound[1]) 

    print("\n--------- Part 3 ---------\n")

    disease_upregulate_gene_count = mapreduce(dict_disease_upregulate_gene)
    top_diseases = sorted(disease_upregulate_gene_count.items(), key = lambda x: x[1], reverse=True)
    print("Top 5 disease based on upregulation with genes:")
    for disease in top_diseases[:5]:
        name_disease = id_to_name(disease[0],nodes_df)
        print(name_disease, disease[1]) 
        
    print("\n---------- Part 5a ----------\n")
    
    r_2 = hashtable_memory_use(compound_bind_gene_count, folding_hash, 2)
    r_3 = hashtable_memory_use(compound_bind_gene_count, folding_hash, 3)

    if r_2 < r_3:
        print("r=2 uses less memory at", r_2, "vs", r_3)
    else:
        print("r=3 uses less memory at", r_3, "vs", r_2)

    print("\n---------- Part 5b ----------\n")

    r_2 = hashtable_memory_use(disease_upregulate_gene_count, folding_hash, 2)
    r_3 = hashtable_memory_use(disease_upregulate_gene_count, folding_hash, 3)

    if r_2 < r_3:
        print("r=2 uses less memory at", r_2, "vs", r_3)
    else:
        print("r=3 uses less memory at", r_3, "vs", r_2)

    
if __name__ == "__main__":
    main()


