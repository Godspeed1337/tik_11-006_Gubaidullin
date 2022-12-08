from operator import itemgetter


def bw_transform(s):
    n = len(s)
    m = sorted([s[n-i:n] + s[0:n-i] for i in range(n)])
    index_ = m.index(s)
    transform_msg = ''.join([q[-1] for q in m])
    return index_, transform_msg


def bw_restore(index_, transform_msg):
    n = len(transform_msg)
    list_1 = sorted([(i, x) for i, x in enumerate(transform_msg)], key=itemgetter(1))

    list_2 = [None for i in range(n)]
    for i, y in enumerate(list_1):
        j, _ = y
        list_2[j] = i

    tx = [index_]
    for i in range(1, n):
        tx.append(list_2[tx[i - 1]])

    result = [transform_msg[i] for i in tx]
    result.reverse()
    return ''.join(result)


if __name__ == "__main__":
    print(bw_restore(24, 'styssesvmrgath  ceiis eee r'))
    print(bw_transform("this is very secret message"))
