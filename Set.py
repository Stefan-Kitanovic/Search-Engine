class Set:
    def __init__(self, elems=[]):
        self.elems = elems

    def append(self, elem):
        if elem not in self.elems:
            self.elems.append(elem)

    def update(self, elems):
        self.elems = elems

    def union(self, set2):
        union_set = Set()

        for elem in self.elems:
            union_set.append(elem)

        for elem in set2.elems:
            if elem not in union_set.elems:
                union_set.append(elem)

        return union_set

    def intersection(self, set2):
        intersection_set = Set()

        for elem in self.elems:
            if elem in set2.elems:
                intersection_set.append(elem)

        for elem in set2.elems:
            if elem in self.elems and elem not in intersection_set.elems:
                intersection_set.append(elem)

        return intersection_set

    def difference(self, set2):
        difference_set = Set()

        for elem in self.elems:
            if elem not in set2.elems:
                difference_set.append(elem)

        return difference_set
