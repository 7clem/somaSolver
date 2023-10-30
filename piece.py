import numpy as np
import math
import unittest

# representing pieces by the positions of the unit cubes, numbered 0 to 26
cee = [0, 1, 3]
ell = [0, 1, 2, 3]
tee = [0, 1, 2, 4]
tri = [0, 1, 3, 9]
ex = cee + [10]
wy = cee + [3 + 9]
zee = [0, 1, 4, 5]

pieces = {'cee': cee, 'ell': ell, 'tee': tee, 'tri': tri, 'ex': ex, 'wy': wy, 'zee': zee}

def index3D(flat):
    z = flat // 9
    y = (flat - 9 * z) // 3
    x = flat % 3
    return x, y, z

def indexFlat(x, y, z):
    return x + y * 3 + z * 9


def list2int(arr: list):
    """arr: list of indices 0 to 26 where a cube is present"""
    return sum([2**n for n in arr])


def int2list(i):
    s = '{:b}'.format(i)
    return [n[0] for n in enumerate(s)]

def list2boolmatrix(arr):
    m = np.zeros((27), np.uint8)
    for c in arr:
        m[c] = 1
    return m.reshape((3, 3, 3))

class Piece:
    """Holds information about one soma piece. It is responsible for its manipulation
    and internal representation"""
    def __init__(self, arr: list):
        # valid data only
        val = dict()
        for key in arr:
            cpt = val.get(key, 0)
            val[key] = cpt + 1

        if any(map(lambda x: x > 1, val.values())):
            raise ValueError("Piece initialized with invalid data. Duplicate.")
        if any(map(lambda x : x < 0 or x > 26, arr)):
            raise ValueError("Value out of bounds. Initializer array data must be  0 <= integer <= 26.")
        if any(map(lambda x : not isinstance(x, int), arr)):
            raise ValueError(f"Initializer array values must all be integers. {arr}")
        self.data = arr

    def __eq__(self, other):
        other = Piece(other)
        return set(self.data) == set(other.data)

    def move(self, dx, dy, dz):
        pass

    def rot(self, rx, ry, rz):
        pass

    def __add__(self, other):
        pass

    def invert(self):
        pass


class SomaTest(unittest.TestCase):
    def SetUp(self):
        pass

    def TearDown(self):
        pass

    def testInit(self):
        t = Piece(ell)
        self.assertEqual(ell, t)

    def testIndex(self):
        for t in range(27):
            x, y, z = index3D(t)
            self.assertEqual(t, indexFlat(x, y, z))

    def testBoolPiece(self):
        mt = list2boolmatrix(tee)
        sub = mt[0, :2, :]
        exp = np.array([[1, 1, 1], [0, 1, 0]])
        same = np.equal(sub, exp)
        self.assertTrue(same.all())

    def testList2int(self):
        self.assertEqual(list2int(cee), 1+2+8)
        self.assertEqual(list2int(ell), 1+2+4+8)

    def testint2list(self):
        self.assertEqual( int2list(1+2+4+8), [0, 1, 2, 3])