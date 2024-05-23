import pandas as pd
import os


class CSVLoader:
    """Base class for loading CSV files."""

    def __init__(self, filepath):
        self.filepath = filepath
        self.df = None

    def load(self):
        """Load CSV file into DataFrame."""
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"The file {self.filepath} does not exist.")
        self.df = pd.read_csv(self.filepath)

    def get_dataframe(self):
        """Return the loaded DataFrame."""
        if self.df is None:
            raise ValueError("DataFrame is not loaded. Call load() method first.")
        return self.df