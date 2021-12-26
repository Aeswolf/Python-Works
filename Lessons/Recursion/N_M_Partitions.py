def partition(n, m):
    """
    :param n: Total number of items
    :param m: number of items to be used for the partitioning
    :return: the number of ways a partition can be achieved
    """
    # Bases cases
    if n == 0:
        return 1

    if m == 0 or n < 0:
        return 0

    return partition(n - m, m) + partition(n, m - 1)


print(partition(0, 1))