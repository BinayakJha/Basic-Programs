# Python3 program to construct string from binary tree

# A binary tree node has data, pointer to left
# child and a pointer to right child
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to construct string from binary tree


def treeToString(root: Node, string: list):

    # base case
    if root is None:
        return

    # push the root data as character
    string.append(str(root.data))

    # if leaf node, then return
    if not root.left and not root.right:
        return

    # for left subtree
    string.append('(')
    treeToString(root.left, string)
    string.append(')')

    # only if right child is present to
    # avoid extra parenthesis
    if root.right:
        string.append('(')
        treeToString(root.right, string)
        string.append(')')


# Driver Code
if __name__ == "__main__":

    # Let us construct below tree
    #		 1
    #	 / \
    #	 2	 3
    #	 / \	 \
    # 4 5	 6

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    string = []
    treeToString(root, string)
    print(''.join(string))
