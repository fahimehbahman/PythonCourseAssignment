import unittest
from unittest.mock import patch, MagicMock
import os
import pandas as pd
from Service.DataProcessor import  DataProcessor
from sqlalchemy import create_engine, MetaData, Table, Column, Float


class TestDataProcessor(unittest.TestCase):

    def setUp(self):
        self.db_folder = 'TestDatabase'
        self.db_name = 'TestPythonTaskDataBase.db'
        self.processor = DataProcessor(db_folder=self.db_folder, db_name=self.db_name)

    def tearDown(self):
        db_path = os.path.join(self.db_folder, self.db_name)
        if os.path.exists(db_path):
            os.remove(db_path)
        if os.path.exists(self.db_folder):
            os.rmdir(self.db_folder)

    def test_create_tables(self):
        with patch.object(self.processor.metadata, 'create_all') as mock_create_all:
            self.processor.create_tables()
            mock_create_all.assert_called_once()

    @patch('pandas.DataFrame.to_sql')
    def test_save_to_db(self, mock_to_sql):
        df = pd.DataFrame({'x': [1, 2, 3], 'y1': [4, 5, 6], 'y2': [7, 8, 9]})
        self.processor.save_to_db(df, 'TestTable')
        mock_to_sql.assert_called_once_with('TestTable', self.processor.engine, if_exists='replace', index=False)

    def test_find_best_fit(self):
        training_df = pd.DataFrame({
            'x': [1, 2, 3],
            'y1': [1, 2, 3],
            'y2': [2, 4, 6]
        })
        ideal_df = pd.DataFrame({
            'x': [1, 2, 3],
            'f1': [1, 2, 3],
            'f2': [2, 4, 6],
            'f3': [3, 6, 9]
        })
        best_fit = self.processor.find_best_fit(training_df, ideal_df)
        expected_best_fit = {'y1': 'f1', 'y2': 'f2'}
        self.assertEqual(best_fit, expected_best_fit)

    def test_calculate_deviation(self):
        test_df = pd.DataFrame({
            'x': [1, 2, 3],
            'y': [1, 2, 3]
        })
        ideal_df = pd.DataFrame({
            'x': [1, 2, 3],
            'f1': [1, 2, 3],
            'f2': [2, 4, 6]
        })
        best_fit_functions = {'y': 'f1'}
        deviations = self.processor.calculate_deviation(test_df, ideal_df, best_fit_functions)
        expected_deviations = [
            (1, 1, 'f1', 0),
            (2, 2, 'f1', 0),
            (3, 3, 'f1', 0)
        ]
        self.assertEqual(deviations, expected_deviations)

if __name__ == '__main__':
    unittest.main()
