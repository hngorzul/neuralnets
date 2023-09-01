"""
DO NOT EDIT THIS FILE !!!
"""
import unittest
from scipy import stats

from src.seminar1 import *


class TestRandomMatrix(unittest.TestCase):

    def setUp(self) -> None:
        self.rm = random_matrix(100)

    def test_shape(self):
        self.assertEqual(self.rm.shape, (100, 100, 3))

    def test_type(self):
        self.assertEqual(self.rm.dtype, np.uint8)

    def test_uniform(self):
        rm = random_matrix(100).ravel()
        ks, p = stats.kstest(rm, stats.uniform(loc=0, scale=255).cdf)
        print(f'KS = {ks:.2f} , p-value = {p:.2f}')
        self.assertLess(ks, 0.1)
        self.assertGreater(p, 0.05)


class TestBroadcastArray(unittest.TestCase):

    def setUp(self) -> None:
        self.expected = np.array([
            np.arange(10),
            np.arange(10),
            np.arange(10),
            np.arange(10),
            np.arange(10)])

    def testShape(self):
        bm = broadcast_array(np.arange(13), 42)
        self.assertEqual(bm.shape, (42, 13))

    def testBroadcast(self):
        bm = broadcast_array(np.arange(10), 5)
        self.assertTrue(np.array_equal(bm, self.expected))


class TestInplaceOperation(unittest.TestCase):

    def testModify(self):
        a = np.eye(3)
        b = np.eye(3)
        a_copy = a.copy()
        inplace_operation(a_copy, b)
        self.assertFalse(np.array_equal(a_copy, a))

    def testEqual(self):
        a = np.eye(3)
        b = np.eye(3)
        new_a = (a + b) * (- a / 2)
        inplace_operation(a, b)
        self.assertTrue(np.array_equal(new_a, a))
        self.assertFalse(new_a is a)


class TestGetElements(unittest.TestCase):

    def setUp(self) -> None:
        self.a = np.arange(25).reshape(5, 5)

    def testGetElements1(self):
        i = np.arange(5)
        elements = get_elements(self.a, i)
        self.assertTrue(np.array_equal(elements, np.array([0, 6, 12, 18, 24])))

    def testGetElements2(self):
        i = np.ones(5, dtype=int)
        elements = get_elements(self.a, i)
        self.assertTrue(np.array_equal(elements, np.array([1, 6, 11, 16, 21])))


class TestInnerProducts(unittest.TestCase):

    def testInner1(self):
        a = np.ones((10, 10))
        sip = self_inners(a)
        self.assertTrue(np.array_equal(a*10, sip))

    def testInner2(self):
        a = np.arange(6)
        b = np.array([a, a, a])
        sip = self_inners(b)
        self.assertEqual(sip.shape, (3, 3))
        self.assertTrue(np.array_equal(sip, np.ones_like(sip)*55))


if __name__ == '__main__':
    unittest.main()