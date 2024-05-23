from Service.CSVLoader import CSVLoader
import pandas as pd

class IdealFunctionLoader(CSVLoader):
    """Class for loading ideal function CSV files."""

    def load(self):
        """Load CSV file and rename columns accordingly."""
        super().load()
        self.df.columns = ['x'] + [f'ideal_y{i}' for i in range(1, 51)]

    def validateCSVColumns(self, file_path):
        try:
            df = pd.read_csv(file_path)
            required_columns = ['x'] + [f'ideal-y{i}' for i in range(1, 51)]
            if list(df.columns) != required_columns:
                raise ValueError(f"IdealFunction CSV file does not have the required columns: {required_columns}")
        except Exception as e:
            raise ValueError(f"Error validating CSV file {file_path}: {e}")
