import functools
import collections
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(tree: BinaryTreeNode, node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    # TODO - you fill in here.
    Status = collections.namedtuple('Status', ('num_target_nodes', 'ancestor'))
    root, p, q = tree, node0, node1
    def helper(node):
        if not node:
            return Status(0, None)
        left = helper(node.left)
        if left.num_target_nodes == 2:
            return left
        right = helper(node.right)
        if right.num_target_nodes == 2:
            return right
        num_target_nodes = left.num_target_nodes + right.num_target_nodes + (p, q).count(node)
        return Status(num_target_nodes, node if num_target_nodes == 2 else None)
    return helper(root).ancestor


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
