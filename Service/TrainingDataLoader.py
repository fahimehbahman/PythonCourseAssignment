import pandas as pd
from Service.CSVLoader import CSVLoader

class TrainingDataLoader(CSVLoader):
    """Class for loading training data CSV files."""

    def load(self):
        """Load CSV file and rename columns accordingly."""
        self.df = pd.read_csv(self.filepath)
        self.df.columns = ['x', 'y1', 'y2', 'y3', 'y4']

    def validateCSVColumns(self, file_path):
        """Validate that the CSV file has the required columns."""
        try:
            df = pd.read_csv(file_path)
            if list(df.columns) != ['x', 'y1', 'y2', 'y3', 'y4']:
                raise ValueError("Training CSV file does not have the required columns: 'x', 'y1', 'y2', 'y3', 'y4'")
        except Exception as e:
            raise ValueError(f"Error validating CSV file {file_path}: {e}")

# Example usage:
# loader = TrainingDataLoader('path/to/training_data.csv', 'y1')
# loader.load()
# print(loader.df)
