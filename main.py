import pandas as pd 
from functools import reduce

def create_dict(dataframe):
    dictionary = {}
    for index,row in dataframe.iterrows():
        dictionary[row["id"]] = []
    return dictionary
def populate_dict(dataframe,dictionary):
    for index,row in dataframe.iterrows():
        dictionary[row["source"]].append(row["target"])
def mapper(compound_binds):
    compound, binds = compound_binds
    return [(compound, 1) for _ in binds]
def reducer(counts, pair):
    compound, bind_count = pair
    counts[compound] = counts.get(compound, 0) + bind_count
    return counts

def main():
    nodes_df = pd.read_csv('nodes_test.tsv', sep='\t')
    edges_df = pd.read_csv('edges_test.tsv', sep='\t')
    compound_nodes_df = nodes_df[nodes_df.kind == "Compound"]
    dict_compounds = create_dict(compound_nodes_df)
    binds_df = edges_df[edges_df.metaedge == "CbG"]
    populate_dict(binds_df,dict_compounds)
    #map data
    mapped_data = reduce(lambda x, y: x + y, map(mapper, dict_compounds.items()))
    #reduce 
    compound_counts = reduce(reducer, mapped_data, {})
    print(compound_counts.get("Compound::DB01268"))
    print(max(compound_counts, key=compound_counts.get))
    
if __name__ == "__main__":
    main()


