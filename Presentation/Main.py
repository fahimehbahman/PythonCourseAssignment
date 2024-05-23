from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox as msg
import pandas as pd
import webbrowser
from Service.DataProcessor import DataProcessor
from Service.IdealFunctionLoader import IdealFunctionLoader
from Service.TestDataLoader import TestDataLoader
from Service.TrainingDataLoader import TrainingDataLoader
from sqlalchemy import create_engine, Column, Float, String, Table, MetaData
import os

class Main:
    def __init__(self, root):
        self.root = root
        self.setup_gui()

    def setup_gui(self):
        self.root.geometry("700x700")
        self.root.resizable(0, 0)
        self.root.title("Main")
        self.root.configure(background="white")

        # Training file 1
        lblPath1 = Label(self.root, text="Training file 1", bg="white")
        lblPath1.grid(row=0, column=0, padx=(10, 10), pady=10)
        button1 = Button(self.root, text="...", command=lambda: self.open_file_dialog(self.entryPath1))
        button1.grid(row=0, column=1, pady=10)
        self.entryPath1 = ttk.Entry(self.root, width=50)
        self.entryPath1.grid(row=0, column=2, padx=(10, 10), pady=10)
        link1 = Label(self.root, text="Download Sample Training1 File", fg="blue", cursor="hand2", bg="white")
        link1.grid(row=0, column=3, padx=(10, 10), pady=10)
        link1.bind("<Button-1>", lambda e: self.open_url(os.path.abspath("SampleInputExcel//Training1.csv")))

        # Training file 2
        lblPath2 = Label(self.root, text="Training file 2", bg="white")
        lblPath2.grid(row=1, column=0, padx=(10, 10), pady=10)
        button2 = Button(self.root, text="...", command=lambda: self.open_file_dialog(self.entryPath2))
        button2.grid(row=1, column=1, pady=10)
        self.entryPath2 = ttk.Entry(self.root, width=50)
        self.entryPath2.grid(row=1, column=2, padx=(10, 10), pady=10)
        link2 = Label(self.root, text="Download Sample Training2 File", fg="blue", cursor="hand2", bg="white")
        link2.grid(row=1, column=3, padx=(10, 10), pady=10)
        link2.bind("<Button-1>", lambda e: self.open_url(os.path.abspath("SampleInputExcel//Training2.csv")))

        # Training file 3
        lblPath3 = Label(self.root, text="Training file 3", bg="white")
        lblPath3.grid(row=2, column=0, padx=(10, 10), pady=10)
        button3 = Button(self.root, text="...", command=lambda: self.open_file_dialog(self.entryPath3))
        button3.grid(row=2, column=1, pady=10)
        self.entryPath3 = ttk.Entry(self.root, width=50)
        self.entryPath3.grid(row=2, column=2, padx=(10, 10), pady=10)
        link3 = Label(self.root, text="Download Sample Training3 File", fg="blue", cursor="hand2", bg="white")
        link3.grid(row=2, column=3, padx=(10, 10), pady=10)
        link3.bind("<Button-1>", lambda e: self.open_url(os.path.abspath("SampleInputExcel//Training3.csv")))

        # Training file 4
        lblPath4 = Label(self.root, text="Training file 4", bg="white")
        lblPath4.grid(row=3, column=0, padx=(10, 10), pady=10)
        button4 = Button(self.root, text="...", command=lambda: self.open_file_dialog(self.entryPath4))
        button4.grid(row=3, column=1, pady=10)
        self.entryPath4 = ttk.Entry(self.root, width=50)
        self.entryPath4.grid(row=3, column=2, padx=(10, 10), pady=10)
        link4 = Label(self.root, text="Download Sample Training4 File", fg="blue", cursor="hand2", bg="white")
        link4.grid(row=3, column=3, padx=(10, 10), pady=10)
        link4.bind("<Button-1>", lambda e: self.open_url(os.path.abspath("SampleInputExcel//Training4.csv")))

        # Function file
        lblFunctionPath = Label(self.root, text="Function file", bg="white")
        lblFunctionPath.grid(row=4, column=0, padx=(10, 10), pady=10)
        buttonFunction = Button(self.root, text="...", command=lambda: self.open_file_dialog(self.entryFunction))
        buttonFunction.grid(row=4, column=1, pady=10)
        self.entryFunction = ttk.Entry(self.root, width=50)
        self.entryFunction.grid(row=4, column=2, padx=(10, 10), pady=10)
        link5 = Label(self.root, text="Download Sample Function File", fg="blue", cursor="hand2", bg="white")
        link5.grid(row=4, column=3, padx=(10, 10), pady=10)
        link5.bind("<Button-1>", lambda e: self.open_url(os.path.abspath("SampleInputExcel//ideal_functions.csv")))

        # Test file
        lblTestPath = Label(self.root, text="Test file", bg="white")
        lblTestPath.grid(row=5, column=0, padx=(10, 10), pady=10)
        buttonTest = Button(self.root, text="...", command=lambda: self.open_file_dialog(self.entryTest))
        buttonTest.grid(row=5, column=1, pady=10)
        self.entryTest = ttk.Entry(self.root, width=50)
        self.entryTest.grid(row=5, column=2, padx=(10, 10), pady=10)
        link6 = Label(self.root, text="Download Sample Test File", fg="blue", cursor="hand2", bg="white")
        link6.grid(row=5, column=3, padx=(10, 10), pady=10)
        link6.bind("<Button-1>", lambda e: self.open_url(os.path.abspath("SampleInputExcel//test_data.csv")))

        btnRegister = Button(self.root, text="Register", command=self.register)
        btnRegister.grid(row=6, column=1, columnspan=2, padx=(10, 10), pady=20)

    def open_file_dialog(self, entry):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
        if file_path:
            entry.delete(0, END)
            entry.insert(END, file_path)

    def open_url(self, url):
        webbrowser.open_new(url)



    def register(self):
        if self.entryPath1.get() == "" or self.entryPath2.get() == "" or self.entryPath3.get() == "" or self.entryPath4.get() == "" or self.entryFunction.get() == "" or self.entryTest.get() == "":
            msg.showinfo("Warning", "Please select all CSV files.")
            return

        filePath1 = self.entryPath1.get()
        filePath2 = self.entryPath2.get()
        filePath3 = self.entryPath3.get()
        filePath4 = self.entryPath4.get()
        fileFunction = self.entryFunction.get()
        fileTest = self.entryTest.get()

        try:

            # create an Instance from class
            ideal_loader = IdealFunctionLoader(fileFunction)
            test_loader = TestDataLoader(fileTest)
            loaders = [TrainingDataLoader(filePath1, 'y1'), TrainingDataLoader(filePath2, 'y2'),
                       TrainingDataLoader(filePath3, 'y3'), TrainingDataLoader(filePath4, 'y4')]

            # Validate CSV columns
            loaders[0].validateCSVColumns(filePath1)
            loaders[1].validateCSVColumns(filePath2)
            loaders[2].validateCSVColumns(filePath3)
            loaders[3].validateCSVColumns(filePath4)
            ideal_loader.validateCSVColumns(fileFunction)
            test_loader.validateCSVColumns(fileTest)

            # Create a SQLite database and tables
            processor = DataProcessor(db_folder='Model', db_name='PythonTaskDataBase.db')
            processor.create_tables()
            # Proceed with other operations...

            # Load training data into the database

            dfs = [loader.load() or loader.get_dataframe() for loader in loaders]

            merged_df = dfs[0]
            for df in dfs[1:]:
                merged_df = pd.merge(merged_df, df, on='x')

            processor.save_to_db(merged_df, 'TrainingData')

            # Load ideal functions data into the database
            ideal_loader.load()
            ideal_df = ideal_loader.get_dataframe()
            processor.save_to_db(ideal_df, 'IdealFunctions')

            # Load test data
            test_loader.load()
            test_df = test_loader.get_dataframe()

            # Find the best fit functions for each training data column
            best_fit_functions = processor.find_best_fit(merged_df, ideal_df)

            # Calculate deviations for test data
            deviations = processor.calculate_deviation(test_df, ideal_df, best_fit_functions)
            deviation_df = pd.DataFrame(deviations, columns=['x', 'y', 'ideal_function', 'deviation'])
            processor.save_to_db(deviation_df, 'TestResults')

            # Print the results
            result_str = "Best fit functions:\n"
            for key, value in best_fit_functions.items():
                result_str += f"The best fit for {key} is {value}\n"
            msg.showinfo("Best Fit Functions", result_str)

            msg.showinfo("Success", "Data successfully loaded into the database and best fit functions identified.")
        except Exception as e:
            msg.showinfo("Error", f"Failed to process CSV files: {str(e)}")

if __name__ == "__main__":
    root = Tk()
    Main(root)
    root.mainloop()
