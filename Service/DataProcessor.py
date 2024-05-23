from sqlalchemy import create_engine, MetaData, Table, Column, Integer, Float, String
import os
import pandas as pd

class DataProcessor:
    def __init__(self, db_folder='Database', db_name='PythonTaskDataBase.db'):
        if not os.path.exists(db_folder):
            os.makedirs(db_folder)
        db_path = f"sqlite:///{os.path.join(db_folder, db_name)}"
        self.engine = create_engine(db_path)
        self.metadata = MetaData()

    def create_tables(self):
        # Example of creating a table
        training_data_table = Table(
            'TrainingData', self.metadata,
            Column('x', Float, primary_key=True),
            Column('y1', Float),
            Column('y2', Float),
            Column('y3', Float),
            Column('y4', Float)
        )
        self.metadata.create_all(self.engine)

    def save_to_db(self, df, table_name):
        df.to_sql(table_name, self.engine, if_exists='replace', index=False)

    def find_best_fit(self, training_df, ideal_df):
        best_fit = {}
        for y_col in training_df.columns[1:]:
            min_deviation = float('inf')
            best_func = None
            for func_col in ideal_df.columns[1:]:
                deviation = ((training_df[y_col] - ideal_df[func_col]) ** 2).sum()
                if deviation < min_deviation:
                    min_deviation = deviation
                    best_func = func_col
            best_fit[y_col] = best_func
        return best_fit

    def calculate_deviation(self, test_df, ideal_df, best_fit_functions):
        deviations = []
        for _, row in test_df.iterrows():
            x_val = row['x']
            y_val = row['y']
            best_func = None
            min_deviation = float('inf')
            for func_col in ideal_df.columns[1:]:
                func_val = ideal_df.loc[ideal_df['x'] == x_val, func_col].values[0]
                deviation = abs(y_val - func_val)
                if deviation < min_deviation:
                    min_deviation = deviation
                    best_func = func_col
            deviations.append((x_val, y_val, best_func, min_deviation))
        return deviations
