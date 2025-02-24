import pandas as pd 

nodes_df = pd.read_csv('nodes_test.tsv', sep='\t')
edges_df = pd.read_csv('edges_test.tsv', sep='\t')

def create_dict(dataframe):
    """
    Creates a dictionary of all the source nodes that we're expecting
    """
    dictionary = {}
    for index,row in dataframe.iterrows():
        dictionary[row["id"]] = []
    return dictionary

def populate_dict(dataframe,dictionary):
    """
    Match the expected source nodes to their target nodes
    """
    for index,row in dataframe.iterrows():
        dictionary[row["source"]].append(row["target"])

def get_relationships(node_type, edge_type):
    """
    Given a source node type and and edge type, 
    returns a dictionary with all the source nodes
    mapped to their corresponding target node
    via the specified edge type.
    """
    source_nodes_df = nodes_df[nodes_df.kind == node_type]
    dict_nodes = create_dict(source_nodes_df)

    relationships_df = edges_df[edges_df.metaedge == edge_type]
    populate_dict(relationships_df, dict_nodes)

    return dict_nodes

def id_to_name(id,dataframe):
    """
    Given a node id, return the node's name
    """
    id_query = dataframe[dataframe.id == id]
    name = next(id_query.iterrows())[1]
    return name["name"]
   

