import unittest


class Try:
    def __init__(self, p):
        self.data = str(p)

    def addTransform(self, tr_str):
        self.data += ', ' + str(tr_str)

    def __bool__(self):
        return False

    def __repr__(self):
        return "Try('{self.data}')"


class TestTry(unittest.TestCase):
    def testOne(self):
        tt = Try("ell, rXr, incX")
        self.assertFalse(tt)
