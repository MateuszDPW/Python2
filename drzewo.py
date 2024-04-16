# Przykladowa tablica reprezentujaca drzewo binarne
tree = [1,2,3,4,5,6,7]

def get_left_child(index):
    # Zwraca lewe dziecko węzła o danym indeksie.
    return 2 * index + 1

def get_right_child(index):
    # Zwraca prawe dziecko węzła o danym indeksie
    return 2 * index + 2

def get_parent(index):
    # zwraca rodzica węzła o danym indeksie
    return (index-1) // 2

# dostęp do elementów drzewa
index = 0 # korzeń drzewa
left_child_index = get_left_child(index)
right_child_index = get_right_child(index)

print(f"Wartość korzenia: {tree[index]}")
print(f"Lewe dziecko korzenia: {tree[left_child_index]}")
print(f"Prawe dziecko korzenia: {tree[right_child_index]}")


# Przykład przeszukiwania w głąb
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def dfs_preorder(node):
        if node:
            print(node.value)           # Odwiedź węzeł
            dfs_preorder(node.left)     # Eksploruj lewe poddrzewo
            dfs_preorder(node.right)    # eksploruj prawe poddrzewo

# Tworzenie przykladowego drzewa
#       1
#      / \
#     2   3
#    / \   
#   4   5

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Rozpoczęcie przeszukiwania w głąb (DFS) z korzenia
print("Przeszukiwanie w głąb (DFS) - Pre-order")
dfs_preorder(root)


# Przykład eksploracja poziom na poziomie
from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def bfs(root):
        if root is None:
            return

    queue = deque([root])

    while queue:
        current_node = queue.popleft()
        print(current_node.value)

        if current_node.left is not None:
            queue.append(current_node.left)
        if current_node.right is not None:
            queue.append(current_node.right)

# Tworzenie przykladowego drzewa
#       1
#      / \
#     2   3
#    / \   \ 
#   4   5   6

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

# wywołanie przeszukiwania wszerz
print("Przeszukiwanie wszerz(BFS):")
bfs(root)
