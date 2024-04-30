import pandas as pd 
from Classes import Compound



def main():

    nodes_df = pd.read_csv('nodes_test.tsv', sep='\t')
    edges_df = pd.read_csv('edges_test.tsv', sep='\t')
    
    list_of_compounds = []
    compound_nodes_df = nodes_df[nodes_df.kind == "Compound"]
    binds_df = edges_df[edges_df.metaedge == "CbG"]
    print(len(binds_df[binds_df.source == "Compound::DB01435"]))
    for index,row in compound_nodes_df.iterrows():
        compound = Compound(row["id"],row["name"])
        list_of_compounds.append(compound)
    
if __name__ == "__main__":
    main()
