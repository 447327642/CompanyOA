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
            'memo': {}
        }


def bfs_with_memo(adj_list, read_time, start):

    node_stack = []
    prev_stack = []
    cur = start
    cur_index = 0
    prev = None
    sum = 0.0

    while len(node_stack) or cur_index < len(adj_list[cur]["adjacents"]):
        adjacents = adj_list[cur]["adjacents"]
        while (prev and len(adjacents) >= 2) or (not prev):
            sum = 0.0
            cur_index = 1 if adjacents[0] == prev else 0
            node_stack.append((prev, cur, cur_index, len(adjacents), sum))
            prev = cur
            cur = adjacents[cur_index]
            adjacents = adj_list[cur]["adjacents"]
        else:
            tmp_cur = cur
            (prev, cur, cur_index, n_count, prev_sum) = node_stack.pop()
            sum = prev_sum + read_time[tmp_cur - 1]
            while cur_index == n_count - 1 or (cur_index == n_count - 2 and adj_list[cur]["adjacents"][-1] == prev):
                if not prev:
                    return sum / n_count + read_time[cur - 1]
                sum = sum / (n_count - 1) + read_time[cur - 1]
                adj_list[cur]['memo'][prev] = sum
                (prev, cur, cur_index, n_count, prev_sum) = node_stack.pop()
                sum += prev_sum
            else:
                cur_index = cur_index + 2 if adj_list[cur]["adjacents"][cur_index + 1] == prev else cur_index + 1
                node_stack.append((prev, cur, cur_index, len(adj_list[cur]["adjacents"]), sum))
                prev = cur
                cur = adj_list[cur]["adjacents"][cur_index]


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
    print adj_list