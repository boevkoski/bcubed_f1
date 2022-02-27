def calculate(partition1, partition2):

    partition1_communities = {}
    partition2_communities = {}

    partition1_nodes = set(partition1.keys())
    partition2_nodes = set(partition2.keys())

    intersection_nodes = partition1_nodes.intersection(partition2_nodes)
    partition1_unique_nodes = partition1_nodes.difference(partition2_nodes)
    partition2_unique_nodes = partition2_nodes.difference(partition1_nodes)

    for node in intersection_nodes:
        partition1_community = partition1[node]
        partition2_community = partition2[node]

        if partition1_community not in partition1_communities:
            partition1_communities[partition1_community] = {node}
        else:
            partition1_communities[partition1_community].add(node)

        if partition2_community not in partition2_communities:
            partition2_communities[partition2_community] = {node}
        else:
            partition2_communities[partition2_community].add(node)

    cumulative_precision = 0
    cumulative_recall = 0
    for node in intersection_nodes:
        partition1_community = partition1[node]
        partition2_community = partition2[node]

        partition1_co_members = partition1_communities[partition1_community]
        partition2_co_members = partition2_communities[partition2_community]

        cumulative_precision += len(partition1_co_members.intersection(partition2_co_members)) / len(partition1_co_members)
        cumulative_recall += len(partition2_co_members.intersection(partition1_co_members)) / len(partition2_co_members)

    precision = cumulative_precision / (len(intersection_nodes) + len(partition1_unique_nodes))
    recall = cumulative_recall / (len(intersection_nodes) + len(partition2_unique_nodes))

    f1 = 2 * (precision * recall) / (precision + recall)

    return f1
