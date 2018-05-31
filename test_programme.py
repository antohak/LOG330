import unittest
from programme import Operations

list = [186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601]
operations = Operations(list)

class TestXAverage(unittest.TestCase):
    def test_average(self):
        # Test avg == 638.9
        self.assertAlmostEqual(operations.average(), 638.9)
class TestVariance(unittest.TestCase):
    def test_variance(self):
        # Test avg == 638.9
        self.assertAlmostEqual(operations.variance(), 391417.8778)

class TestStandardDeviation(unittest.TestCase):
    def test_standardDeviation(self):
        # Test avg == 638.9
        self.assertAlmostEqual(operations.standard_deviation(), 625.63)
