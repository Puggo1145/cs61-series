def tree(label: int, branches=[]):
    for branch in branches:
        assert is_tree(branch), "branches must be trees"
    return [label] + list(branches)


def label(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_tree(tree):
    # check the type of tree and if there is at least one node in the tree
    if type(tree) != list or len(tree) < 1:
        return False
    # check every branch in the tree
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    return not branches(tree)


# tree processing
def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        return sum([count_leaves(branch) for branch in branches(tree)])


def leaves(tree):
    """Return a list containing the leaf labels of a tree"""
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(branch) for branch in branches(tree)], [])


def increment(t):
    return tree(label(t) + 1, [increment(branch) for branch in branches(t)])


def increment_leaves(t):
    if is_leaf(t):
        return [label(t) + 1]
    else:
        bs = [increment_leaves(branch) for branch in branches(t)]
        return tree(label(t), bs)
    
    
def print_tree(t, indent=0):
    print("  "*indent + str(label(t)))
    for branch in branches(t):
        print_tree(branch, indent+1)


def fib_tree(n: int):
    if n <= 1:
        return tree(n)
    else:
        left = fib_tree(n - 1)
        right = fib_tree(n - 2)
        return tree(label(left) + label(right), [left, right])

