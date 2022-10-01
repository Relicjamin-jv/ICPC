import math
import os
import heapq as heap


def main():
    input_file_path = os.path.join('Day 15','input')
    outfile = open(input_file_path, 'r')
    data = outfile.readlines()
    arr = []
    pointer = 0
    for line in data:
        arr.append([])
        for digit in line:
            if digit != "\n":
                arr[pointer].append(int(digit))
        pointer += 1

    print("Smaller cave")
    returnVal = astar(arr)
    print(returnVal)

    print("Larger cave")
    larger_cave = extend_array(arr)
    returnValLarger = astar(larger_cave)
    print(returnValLarger)


def astar(cave):
    start_node = (0, 0)
    end_node = (len(cave[0]) - 1, len(cave[0]) - 1)

    open_queue = []
    closed_queue = set()
    parents = {}
    g_score = {}

    for x in range(len(cave)):
        for y in range(len(cave)):
            g_score[(x, y)] = math.inf

    g_score[start_node] = 0
    heap.heappush(open_queue, (get_city_block(start_node, end_node), start_node))

    while open_queue:
        _, node = heap.heappop(open_queue)

        if node == end_node:
            total = 0
            while node in parents:
                x = node[0]
                y = node[1]
                total += cave[x][y]
                node = parents[node]
            return total

        elif node in closed_queue:
            continue

        else:
            neighbors = get_neighbors(cave, node)

            for n in neighbors:
                if n in closed_queue:
                    continue
                x = n[0]
                y = n[1]
                n_g_score = cave[x][y]

                candidate = g_score[node] + n_g_score

                if candidate <= g_score[n]:
                    g_score[n] = candidate
                    parents[n] = node
                    f = get_city_block(n, end_node) + candidate
                    heap.heappush(open_queue, (f, n))
        closed_queue.add(node)


def get_neighbors(cave, node):
    x = node[0]
    y = node[1]
    node_neighbors = []

    neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

    for i in neighbors:
        if 0 <= i[0] < len(cave) and 0 <= i[1] < len(cave):
            node_neighbors.append(i)

    return node_neighbors


def get_city_block(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def extend_array(cave):
    array_length = len(cave)
    max_list_size = array_length * 5
    extended_array = [[0 for i in range(max_list_size)] for j in range(max_list_size)]

    for x in range(max_list_size):
        for y in range(max_list_size):
            untransposed_data = cave[x % array_length][y % array_length]
            extended_array[x][y] = (untransposed_data + (x // array_length + y // array_length) - 1) % 9 + 1


    return extended_array


if __name__ == "__main__":
    # executed when ran through the cmd line
    main()
