from functools import reduce

def mapper(nodes_edges):
    """
    Turns each edge into a 1 count
    """
    node, edge = nodes_edges
    return [(node, 1) for _ in edge]

def reducer(counts, pair):
    """
    Accumulates counts of edges for nodes
    """
    node, edge_count = pair
    counts[node] = counts.get(node, 0) + edge_count
    return counts

def mapreduce(dictionary):
    """
    Takes a dictionary of source nodes mapped to its corresponding target nodes, 
    and will read the key-value pairs from it, 
    and process through the MapReduce algorithm, 
    to count the number of relationships each source node has.
    """
    # map
    mapped_data = reduce(lambda x, y: x + y, map(mapper, dictionary.items()))

    # reduce 
    relationship_counts = reduce(reducer, mapped_data, {})

    return relationship_counts