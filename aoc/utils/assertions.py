from unittest import TestCase

_tc = TestCase()


def asserteq(a, b):
    _tc.assertEqual(a, b)


def assertt(a):
    _tc.assertTrue(a)
