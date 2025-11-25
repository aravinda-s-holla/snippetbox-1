import threading
from concurrent.futures import Executor, as_completed


# Create a Lock object

class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None


class TreeSizeCalculator:
    def __init__(self, root: Node, executor: Executor):
        self.root = root
        self.executor = executor
        self.size = 0
        self._lock = threading.Lock()

    def calculate_size(self):
        # Todo for leaners
        if self.root is None:
            return

        self._calculate_size_recursive(self.root)

        return self.size

    def _calculate_size_recursive(self, node: Node):

        futures = []
        if node.left:
            futures.append(self.executor.submit(self._calculate_size_recursive, node.left))
            # self._calculate_size_recursive(self.root.left)

        if node.right:
            futures.append(self.executor.submit(self._calculate_size_recursive, node.right))
            # self._calculate_size_recursive(self.root.right)

        # print(futures)
        for f in as_completed(futures):
            f.result()

        with self._lock:
            self.size += 1
