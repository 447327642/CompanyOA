# I was rejected in resume screening phase, so if you needed me to solve more
# problems in order to get a phone interview, please let me know, and I will
# try my best to solve them.

__author__ = 'WANG. Cheng'


def save_relation(adj_list, nodeA, nodeB):
    if nodeA in adj_list:
        adj_list[nodeA]['adjacents'].append(nodeB)
    else:
        adj_list[nodeA] = {
            'adjacents': [nodeB],
            'memo': []
        }


def bfs_with_memo(adj_list, read_time, start, prev=None):

    result = read_time[start - 1]
    adjacents = adj_list[start]['adjacents']
    neighbor_count = len(adjacents)

    while (prev and neighbor_count <= 2) or (not prev and neighbor_count == 1):
        if prev:
            if neighbor_count == 1:
                return result
            else:
                next = adjacents[0] if adjacents[0] != prev else adjacents[1]
        else:
            next = adjacents[0]
        result += read_time[next - 1]
        adjacents = adj_list[next]['adjacents']
        neighbor_count = len(adjacents)
        prev = start
        start = next
    else:
        prob = 1.0 / (neighbor_count - 1) if prev else 1.0 / neighbor_count
        for adj_node in adj_list[start]['adjacents']:
            if adj_node != prev:
                result += prob * bfs_with_memo(adj_list, read_time, adj_node, start)

    return result

if __name__ == "__main__":

    q_count = int(raw_input())
    q_read_time = [int(i) for i in raw_input().split()]
    adj_list = {}
    for i in range(q_count - 1):
        node, adj_node = raw_input().split()
        node = int(node)
        adj_node = int(adj_node)
        save_relation(adj_list, node, adj_node)
        save_relation(adj_list, adj_node, node)

    opt_start = -1
    min_time = -1
    for i in range(q_count):
        ith_result = bfs_with_memo(adj_list, q_read_time, i + 1)
        print ith_result
        if min_time == -1 or min_time > ith_result:
            opt_start = i + 1
            min_time = ith_result


    print opt_start