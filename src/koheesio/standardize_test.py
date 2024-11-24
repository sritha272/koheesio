import unittest
from standardisation import standardize, StandardizeConfig

class TestStandardize(unittest.TestCase):

    def test_standardize_identical_values(self):
        data = [10, 10, 10]
        config = StandardizeConfig()
        with self.assertRaises(ValueError):
            standardize(data, config)

    def test_standardize_with_precomputed_values(self):
        """Test standardization with precomputed mean and standard deviation."""
        data = [10, 20, 30]
        config = StandardizeConfig(mean=20, std_dev=10)
        result = standardize(data, config)
        expected = [-1.0, 0.0, 1.0]
        self.assertEqual(result, expected)

    def test_standardize_empty_data(self):
        """Test standardization with an empty data list."""
        data = []
        config = StandardizeConfig()
        with self.assertRaises(ValueError):
            standardize(data, config)


    def test_standardize_with_custom_mean_and_std_dev(self):
        """Test standardization with a custom mean and standard deviation."""
        data = [1, 2, 3, 4, 5]
        config = StandardizeConfig(mean=3, std_dev=1)
        result = standardize(data, config)
        expected = [-2.0, -1.0, 0.0, 1.0, 2.0]
        self.assertEqual(result, expected)
    
    def test_standardize_with_small_variance(self):
        """Test standardization with a dataset having a small variance."""
        data = [1.001, 1.002, 1.003, 1.004, 1.005]
        config = StandardizeConfig()
        result = standardize(data, config)
        self.assertAlmostEqual(sum(result), 0, places=5)  # The sum of standardized values should be near 0

if __name__ == "__main__":
    unittest.main()