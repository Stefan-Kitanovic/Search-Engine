class Set():
    def __init__(self, elems = []):
        self.elems = elems

    def append(self, elem):
        self.elems.append(elem)

    def update(self, elems):
        self.elems = elems


def union(set1, set2):
    union_set = Set([])

    for elem in set1.elems:
        union_set.append(elem)

    for elem in set2.elems:
        if elem not in union_set.elems:
            union_set.append(elem)

    return union_set


def intersection(set1, set2):
    intersection_set = Set([])

    for elem in set1.elems:
        if elem in set2.elems:
            intersection_set.append(elem)

    for elem in set2.elems:
        if elem in set1.elems and elem not in intersection_set.elems:
            intersection_set.append(elem)

    return intersection_set


def difference(set1, set2):
    difference_set = Set([])

    for elem in set1.elems:
        if elem not in set2.elems:
            difference_set.append(elem)

    return difference_set
