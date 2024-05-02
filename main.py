import pandas as pd 
from functools import reduce

nodes_df = pd.read_csv('nodes_test.tsv', sep='\t')
edges_df = pd.read_csv('edges_test.tsv', sep='\t')
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
def get_relationships(node_type, edge_type):
    """
    Given a source node type and and edge type, 
    returns a dictionary with all the source nodes
    mapped to their corresponding target node
    via the specific edge type.
    """
    
    source_nodes_df = nodes_df[nodes_df.kind == node_type]
    dict_nodes = create_dict(source_nodes_df)
    relationships_df = edges_df[edges_df.metaedge == edge_type]
    populate_dict(relationships_df, dict_nodes)
    return dict_nodes

def main():
    dict_compounds = get_relationships("Compound","CbG")
    # map data
    mapped_data = reduce(lambda x, y: x + y, map(mapper, dict_compounds.items()))
    # reduce 
    compound_counts = reduce(reducer, mapped_data, {})
    print(compound_counts.get("Compound::DB01268"))
    #Top 5 
    #print(compound_counts.items())
    top_compounds = sorted(compound_counts.items(), key= lambda x: x[1],reverse=True)
    print("The top 5 compounds are ", top_compounds[:5])
if __name__ == "__main__":
    main()


