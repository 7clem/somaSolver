import unittest

mapping = dict()
mapping["noop"] = dict(zip(range(27), [0, 1, 2, 3, 4, 5, 6, 7, 8,
                   9, 10, 11, 12, 13, 14, 15, 16, 17,
                   18, 19, 20, 21, 22, 23, 24, 25, 26]))

mapping['incX'] = dict(zip(range(27), [1, 2, None, 4, 5, None, 7, 8, None,
                   10, 11, None, 13, 14, None, 16, 17, None,
                   19, 20, None, 22, 23, None, 25, 26, None]))

mapping['decX'] = dict(zip(range(27), [None, 0, 1, None, 3, 4, None, 6, 7,
                   None, 9, 10, None, 12, 13, None, 15, 16,
                   None, 18, 19, None, 21, 22, None, 24, 25]))

mapping['incY'] = dict(zip(range(27), [3, 4, 5, 6, 7, 8, None, None, None,
                   12, 13, 14, 15, 16, 17, None, None, None,
                   21, 22, 23, 24, 25, 26, None, None, None]))

mapping['decY'] = dict(zip(range(27), [None, None, None, 0, 1, 2, 3, 4, 5,
                   None, None, None, 9, 10, 11, 12, 13, 14,
                   None, None, None, 18, 19, 20, 21, 22, 23]))

mapping['incZ'] = dict(zip(range(27), [9, 10, 11, 12, 13, 14, 15, 16, 17,
                   18, 19, 20, 21, 22, 23, 24, 25, 26,
                   None, None, None, None, None, None, None, None, None]))

mapping['decZ'] = dict(zip(range(27), [None, None, None, None, None, None, None, None, None,
                   0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]))

mapping['rXr'] = dict(zip(range(27), [18, 19, 20, 9, 10, 11, 0, 1, 2,
                  21, 22, 23, 12, 13, 14, 3, 4, 5,
                  24, 25, 26, 15, 16, 17, 6, 7, 8]))

mapping['rXl'] = dict(zip(range(27), [6, 7, 8, 15, 16, 17, 24, 25, 26,
                  3, 4, 5, 12, 13, 14, 21, 22, 23,
                  0, 1, 2, 9, 10, 11, 18, 19, 20]))

mapping['rYr'] = dict(zip(range(27), [18, 9, 0, 21, 12, 3, 24, 15, 6,
                  19, 10, 1, 22, 13, 4, 25, 16, 7,
                  20, 11, 2, 23, 14, 5, 26, 17, 8]))

mapping['rYl'] = dict(zip(range(27), [2, 11, 20, 5, 14, 23, 8, 17, 26,
                  1, 10, 19, 4, 13, 22, 7, 16, 25,
                  0, 9, 18, 3, 12, 21, 6, 15, 24]))

mapping['rZr'] = dict(zip(range(27), [2, 5, 8, 1, 4, 7, 0, 3, 6,
                  11, 14, 17, 10, 13, 16, 9, 12, 15,
                  20, 23, 26, 19, 22, 25, 18, 21, 24]))

mapping['rZl'] = dict(zip(range(27), [6, 3, 0, 7, 4, 1, 8, 5, 2,
                  15, 12, 9, 16, 13, 10, 17, 14, 11,
                  24, 21, 18, 25, 22, 19, 26, 23, 20]))


def f(fname):
    d = mapping[fname]
    return lambda i: d.get(i, None)


def apply(fname: str, i):
    return list(map(f(fname), i))


def domain(fname):
    d = mapping[fname]
    return [int(k) for k, v in d.items() if v is not None]


def way_and_back(way: str, back: str) -> list:
    x = domain(way)
    f1 = apply(way, x)
    return apply(back, f1)


def compose(fnames):
    print(f'compose: fnames={fnames}')
    m = range(27)
    for fname in fnames:
        assert fname in mapping
        m = apply(fname, m)
        print(f'(compose: m = {m}')
    return f(m)



class OpsTest(unittest.TestCase):
    def testDomain(self):
        dom = domain('noop')
        self.assertEqual(dom, list(range(27)))
        d = domain('incX')
        self.assertEqual(d, [0, 1, 3, 4, 6, 7,
                                    9, 10, 12, 13, 15, 16,
                                    18, 19, 21, 22, 24, 25])

    def testNoop(self):
        f = apply('noop', range(27))
        self.assertEqual(f, list(range(27)))

    def testIncX(self):
        x = range(27)
        fx = apply('incX', x)
        ffx = apply('incX', fx)
        self.assertEqual(ffx, [2, None, None, 5, None, None, 8, None, None,
                                      11, None, None, 14, None, None, 17, None, None,
                                      20, None, None, 23, None, None, 26, None, None])

    def testTXWayAndBack(self):
        x = domain('incX')
        self.assertEqual(x, way_and_back('incX', 'decX'), "_incX._decX")

    def testTransformationsWayAndBack(self):
        ops = [['incX', 'decX'],
               ['incY', 'decY'],
               ['incZ', 'decZ'],
               ['rXr', 'rXl'],
               ['rYr', 'rYl'],
               ['rZr', 'rZl']]
        for first, second in ops:
            x = domain(first)
            self.assertEqual(x, way_and_back(first, second), f"{first}.{second}")
            x = domain(second)
            self.assertEqual(x, way_and_back(second, first), f"{second}.{first}")

    def testRotations4Times(self):
        for fname in mapping:
            if fname[0] != 'r':
                continue
            x = domain(fname)
            for _ in range(4):  # 3 other times makes 4
                x = apply(fname, x)
            self.assertEqual(x, domain(fname), f'{fname} applied 4 times should be identity.')

    # def testCompose(self):
    #     transformations = ['incX', 'rXr', 'rZl', 'rZl', 'decX']
    #     testcube = [0, 1, 2, 4]
    #     f = compose(transformations)
    #     rotatedcube = apply(f, testcube)
    #     print(rotatedcube)
