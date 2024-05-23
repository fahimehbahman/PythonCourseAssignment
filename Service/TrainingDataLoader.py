from Service.CSVLoader import CSVLoader
import pandas as pd


class TrainingDataLoader(CSVLoader):
    """Class for loading training data CSV files."""

    def __init__(self, filepath, col_name):
        super().__init__(filepath)
        self.col_name = col_name

    def load(self):
        """Load CSV file and rename columns accordingly."""
        super().load()
        self.df.columns = ['x', self.col_name]

    def validateCSVColumns(self, file_path):
        try:
            df = pd.read_csv(file_path)
            if list(df.columns) != ['X', 'Y']:
                raise ValueError("Training CSV file does not have the required columns: 'X' and 'Y'")
        except Exception as e:
            raise ValueError(f"Error validating CSV file {file_path}: {e}")