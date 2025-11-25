import unittest
from .treeSize import TreeSizeCalculator,Node

class TestTreeSizeCalculator(unittest.TestCase):
    def test_tree_size(self):
        # Creating a binary tree
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        # Now, the as_completed function is used to iterate over the futures returned by the executor,
        # ensuring that we wait for all threads to finish before asserting the size of the binary tree.
        import concurrent.futures
        with concurrent.futures.ThreadPoolExecutor() as executor:
            tree_calculator = TreeSizeCalculator(root, executor)
            tree_calculator.calculate_size()

        self.assertEqual(tree_calculator.size, 7)

if __name__ == '__main__':
    unittest.main()