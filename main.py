import pandas as pd 

def create_dict(dataframe):
    dictionary = {}
    for index,row in dataframe.iterrows():
        dictionary[row["id"]] = []
    return dictionary
def populate_dict(dataframe,dictionary):
    for index,row in dataframe.iterrows():
        dictionary[row["source"]].append(row["target"])

def main():
    checker = input("Enter a compound:")
    nodes_df = pd.read_csv('nodes_test.tsv', sep='\t')
    edges_df = pd.read_csv('edges_test.tsv', sep='\t')
    compound_nodes_df = nodes_df[nodes_df.kind == "Compound"]
    dict_compounds = create_dict(compound_nodes_df)
    binds_df = edges_df[edges_df.metaedge == "CbG"]
    populate_dict(binds_df,dict_compounds)
    
    
if __name__ == "__main__":
    main()
