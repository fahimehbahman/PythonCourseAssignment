from Service.CSVLoader import CSVLoader
import pandas as pd

class TestDataLoader(CSVLoader):
    """Class for loading test data CSV files."""

    def load(self):
        """Load CSV file and rename columns accordingly."""
        super().load()
        self.df.columns = ['x', 'y']

    def validateCSVColumns(self, file_path):
        try:
            df = pd.read_csv(file_path)
            if list(df.columns) != ['x', 'y']:
                raise ValueError("Test CSV file does not have the required columns: 'X' and 'Y'")
        except Exception as e:
            raise ValueError(f"Error validating CSV file {file_path}: {e}")