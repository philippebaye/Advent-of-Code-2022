'''
this script need python 3.10 or higher
'''

import sys

input_file_name = "day7_input_sample.txt" if "SAMPLE" in sys.argv else "day7_input.txt"


#==========================
# Storage of tree structure
#==========================
# size of each nodes, initialized with empty root-node
nodes_size = { "/": 0}
# list of nodes that have no child node
ending_nodes = []
# dictionnary : for each node, its parent node
nodes_and_parent_node = { "/": "/" }
# dictionnary : for each node, the list of its children nodes
nodes_and_children = {"/": []}


ROOT_NODE = "/"

#=======================================================================================
# Discover tree structure and calculate cumulative size of files contained in each nodes
#=======================================================================================
with open(input_file_name) as input_file:
    for command in input_file:
        match command.strip().split():
            case ["$", "cd", "/"]:
                ##print("goto home")
                parent_node, current_node = ROOT_NODE, ROOT_NODE

            case ["$", "cd", ".."]:
                current_node = parent_node
                parent_node = nodes_and_parent_node[current_node]
                ##print(f"goto .. : {current_node}")

            case ["$", "ls"]:
                ending_nodes.append(current_node)   # add to ending_nodes while no dir list in
                ##print("ls")

            case ["$", "cd", directory]:
                parent_node = current_node
                current_node = parent_node + "/" + directory
                nodes_size[current_node] = 0    # initialize the size with 0 (for now no information about files in it)
                nodes_and_parent_node[current_node] = parent_node
                nodes_and_children[parent_node].append(current_node)
                nodes_and_children[current_node] = []
                ##print(f"goto {directory} : {parent_node}->{current_node}")

            case ["dir", directory]:
                if current_node in ending_nodes: ending_nodes.remove(current_node)  # current dir contains children nodes
                ##full_path_directory = current_node + "/" + directory
                ##print(f"dir {directory} : {full_path_directory}")

            case [size, thefile]:
                nodes_size[current_node] += int(size)
                ##print(f"fichier : {thefile}:{size} {current_node}={nodes_size[current_node]}")

print("-------------------------")
print(f"nodes count: {len(nodes_size)}")


#================================================================
# Cumulate, for each node, the size of each of its children nodes
#================================================================
# size of each node, including size of its children nodes
nodes_full_size = {}

def process_node_level(root_node:str) -> int:
    root_node_size = nodes_size[root_node]

    for node in nodes_and_children[root_node]:
        root_node_size += process_node_level(node)

    nodes_full_size[root_node] = root_node_size

    return root_node_size


process_node_level(ROOT_NODE)


#================================
# Calculate minimum space to free
#================================
TOTAL_DISK_SPACE  = 70_000_000
UNUSED_NEED_SPACE = 30_000_000

actual_used_space = nodes_full_size[ROOT_NODE]
minimum_space_to_free = UNUSED_NEED_SPACE - (TOTAL_DISK_SPACE - actual_used_space)

print(f"actual used space: {actual_used_space}")
print(f"minimum space to free: {minimum_space_to_free}")


#================================================================
# Identify nodes, that size is greater than minimum space to free
#================================================================
candidate_nodes = {node: full_size for node, full_size in nodes_full_size.items() if full_size > minimum_space_to_free}
best_candidate = sorted(candidate_nodes.items(), key=lambda x:x[1])[0]

print(f"best candidate: {best_candidate}")
print("-------------------------")
