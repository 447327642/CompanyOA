# If you needed me to solve more problems in order to get
# a phone interview, please let me know, and I will try my
# best to solve them.

# This algorithm works like an inorder traversal iteratively
# Once a node is computed, its value is memorized such that
# we don't need to compute it again.


def save_relation(_adj_list, node_a, node_b):
    if node_a in _adj_list:
        _adj_list[node_a]['neighbors'].append(node_b)
    else:
        _adj_list[node_a] = {
            'neighbors': [node_b],
            'memo': {}
        }


def inorder_with_memo(adj_list, read_time, start):

    node_stack = []
    cur = start
    prev = None

    while True:
        neighbors = adj_list[cur]["neighbors"]
        memo = adj_list[cur]["memo"]

        # See whether this branch has been cached, if not, we go into this branch
        # and push the parent node to the stack
        while (prev not in memo) and len(neighbors) >= 2:
            sum = 0.0
            cur_index = 1 if neighbors[0] == prev else 0
            node_stack.append((prev, cur, cur_index, len(neighbors), sum))
            prev = cur
            cur = neighbors[cur_index]
            neighbors = adj_list[cur]["neighbors"]
            memo = adj_list[cur]["memo"]
        else:
            # One of the branches reaches the end. We pop the parent node and add the readtime
            # to the parent node
            sum = (read_time[cur - 1] if prev not in memo else memo[prev])
            (prev, cur, cur_index, n_count, prev_sum) = node_stack.pop()
            sum += prev_sum

            # Check if all children have been visited. If so, we pop the parent node, update the sum, and
            # cache the result. If not, we move to the next child.
            while cur_index == n_count - 1 or (cur_index == n_count - 2 and adj_list[cur]["neighbors"][-1] == prev):
                sum = sum / (n_count - 1) + read_time[cur - 1]
                if not prev:
                    return sum

                adj_list[cur]['memo'][prev] = sum

                (prev, cur, cur_index, n_count, prev_sum) = node_stack.pop()
                sum += prev_sum
            else:
                neighbors = adj_list[cur]["neighbors"]
                cur_index = cur_index + 2 if neighbors[cur_index + 1] == prev else cur_index + 1
                node_stack.append((prev, cur, cur_index, n_count, sum))
                prev = cur
                cur = neighbors[cur_index]

# The graph(tree) is stored using adjacent list.
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
        if (len(adj_list[i + 1]["neighbors"]) > 1):
            adj_list[i + 1]["neighbors"].append(None)
            ith_result = inorder_with_memo(adj_list, q_read_time, i + 1)
            if min_time == -1 or min_time > ith_result:
                opt_start = i + 1
                min_time = ith_result
            adj_list[i + 1]["neighbors"].pop()
            #print ith_result

    print opt_start