# CSCI 493.76: Big Data Technologies
# Project 2
# Steven Hsui, Victor Yuen

## Part 1

### Question

Readin nodes.tsv and edges.tsv. Find ”tsv” is short for Tab Separated Values, where each values (text or numerical values) are separated by a TAB. You can choose the data structure type to store the values (pyspark or pandas).

### Pseudocode

```
nodes_df = pandas.read_csv("nodes.tsv", '\t')
edges_df = pandas.read_csv("edges.tsv", '\t')

dictionary = {}

source_nodes_df = nodes_df[kind == source_node_type]
for item in source_nodes_df:
    dictionary[item[id]] = []

relationships_df = edges_df[metaedge == edge_type]
for item in relationships_df:
    dictionary[item[source]].append(item[target])

return dictionary
```

### Output

(N/A)

## Part 2

### Question

For each compound, compute the number of genes that are BIND (CbG) to it using MapReduce method. Output results with top 5 number of genes in a descending order. See example for Figure 1

### Pseudocode

```
node, edge = dict_CbG.items()
initial_counts = [(node, 1) for _ in edge]

counts = {}
node, edge_count = initial_counts
counts[node] = counts.get(node, 0) + edge_count

sort(counts)

for compound of counts.items()[:5]:
    print(nodes_df[id == compound[0].id][name], compound[1])
```

### Output

```
Top 5 compounds based on bindings with genes:
Sunitinib 132
Bosutinib 104
Crizotinib 85
Dasatinib 64
Metformin 56
```

## Part 3

### Question

For each DISEASE, compute the number of GENE(s) that are UPREGULATES (DuG) using MapReduce method. Output results with the top 5 number of GENE(s) in a descending order. See example for Figure 2.

### Pseudocode

```
node, edge = dict_DuG.items()
initial_counts = [(node, 1) for _ in edge]

counts = {}
node, edge_count = initial_counts
counts[node] = counts.get(node, 0) + edge_count

sort(counts)

for disease of counts.items()[:5]:
    print(nodes_df[id == disease[0].id][name], disease[1])
```

### Output

```
Top 5 compounds based on bindings with genes:
Sunitinib 132
Bosutinib 104
Crizotinib 85
Dasatinib 64
Metformin 56
```

## Part 5

### Question

For item number 2 to 4 above, compute the hash tables using mid-square method (with r = 3, 4) OR Folding Method (digit-size = 2 and 3). Experiment with 10 hash tables for the selected method. Which method (which digit-size?, r = 3 or r = 4) require least number of storage? Use sys.getsizeof(.) to find the size of the hash tables (10) with its associated link list(s).

Picked Folding Method

### Pseudocode

```
goes here
```

### Output

```
goes here
```

## References
- MapReduce_Count_Friends.py from course Blackboard
- Pandas documentation: https://pandas.pydata.org/docs/