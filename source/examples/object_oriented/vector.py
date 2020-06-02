"""
Vector type with +, * redefined as Vector addition and dot product
"""


class Vector(list):
    def __repr__(self):
        """
        String representation, uses list (superclass) representation
        """
        return 'Vector({})'.format(super().__repr__())

    def __add__(self, v):
        """
        redefine + as element-wise Vector sum
        """
        if len(self) != len(v):
            raise TypeError("Vector can only be added to a sequence of the same length")
        else:
            return Vector([x1 + x2 for x1, x2 in zip(self, v)])

    def __mul__(self, v):
        """
        redefine * as Vector dot product
        """
        if len(self) != len(v):
            raise TypeError("Vector can only be multiplied with a sequence of the same length")
        else:
            return sum([x1 * x2 for x1, x2 in zip(self, v)])


if __name__ == '__main__':
    l1 = [1, 2, 3]
    l2 = [4, 5, 6]
    v1 = Vector(l1)
    v2 = Vector(l2)

    print('l1')
    print(l1)
    print('l1 + l2')
    print(l1 + l2)
    # print(l1 * l2) # TypeError
    print('zip(l1, l2)')
    print(zip(l1, l2))
    print('v1')
    print(v1)
    print('v1 + v2')
    print(v1 + v2)
    print('v1 * v2')
    print(v1 * v2)
