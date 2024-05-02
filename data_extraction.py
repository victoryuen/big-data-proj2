import pandas as pd 

def create_dict(dataframe):
    dictionary = {}
    for index,row in dataframe.iterrows():
        dictionary[row["id"]] = []
    return dictionary

def populate_dict(dataframe,dictionary):
    for index,row in dataframe.iterrows():
        dictionary[row["source"]].append(row["target"])

def get_relationships(node_type, edge_type):
    """
    Given a source node type and and edge type, 
    returns a dictionary with all the source nodes
    mapped to their corresponding target node
    via the specific edge type.
    """
    nodes_df = pd.read_csv('nodes_test.tsv', sep='\t')
    edges_df = pd.read_csv('edges_test.tsv', sep='\t')

    source_nodes_df = nodes_df[nodes_df.kind == node_type]
    dict_nodes = create_dict(source_nodes_df)

    relationships_df = edges_df[edges_df.metaedge == edge_type]
    populate_dict(relationships_df, dict_nodes)

    return dict_nodes