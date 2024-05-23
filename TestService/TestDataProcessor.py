import unittest
import pandas as pd
from my_project.services.data_processor import DataProcessor

class TestDataProcessor(unittest.TestCase):

    def setUp(self):
        self.processor = DataProcessor()

    def test_find_best_fit(self):
        training_data = {
            'x': [1, 2, 3],
            'y1': [2, 4, 6],
            'y2': [1, 2, 3]
        }
        ideal_functions = {
            'x': [1, 2, 3],
            'ideal_y1': [2, 4, 6],
            'ideal_y2': [1, 2, 3]
        }
        training_df = pd.DataFrame(training_data)
        ideal_df = pd.DataFrame(ideal_functions)
        best_fit_functions = self.processor.find_best_fit(training_df, ideal_df)
        expected_best_fit = {'y1': 'ideal_y1', 'y2': 'ideal_y2'}
        self.assertEqual(best_fit_functions, expected_best_fit)

    def test_calculate_deviation(self):
        test_data = {
            'x': [1, 2, 3],
            'y': [2.1, 3.9, 6.1]
        }
        ideal_functions = {
            'x': [1, 2, 3],
            'ideal_y1': [2, 4, 6],
            'ideal_y2': [1, 2, 3]
        }
        best_fit_functions = {'y': 'ideal_y1'}
        test_df = pd.DataFrame(test_data)
        ideal_df = pd.DataFrame(ideal_functions)
        deviations = self.processor.calculate_deviation(test_df, ideal_df, best_fit_functions)
        expected_deviation = [
            [1, 2.1, 'ideal_y1', 0.1],
            [2, 3.9, 'ideal_y1', 0.1],
            [3, 6.1, 'ideal_y1', 0.1]
        ]
        self.assertEqual(deviations, expected_deviation)
