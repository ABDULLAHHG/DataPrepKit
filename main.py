import pandas as pd

class DataProcessor:
    def init(self, file_path: str):
        self.file_path = file_path
        self.file_extension = self.file_path.rsplit(".", 1)[-1].lower()
        self.df = None

    def read_data(self)  -> None :
        try:
            if self.file_extension == "csv":
                self.df = pd.read_csv(self.file_path)
            elif self.file_extension == "excel":
                self.df = pd.read_excel(self.file_path)
            elif self.file_extension == "json":
                self.df = pd.read_json(self.file_path)
            else:
                raise ValueError(f"Unsupported file extension: {self.file_extension}")
        except (FileNotFoundError, pd.errors.ParserError) as e:
            print(f"Error reading data: {e}")

    def encode_column(self, column_name: str, encoding_method: str) -> None:
        if encoding_method == "categorical":
            self.df[column_name] = self.df[column_name].astype("category")
            self.df[column_name] = self.df[column_name].cat.codes
        elif encoding_method == "one-hot":
            self.df = pd.get_dummies(self.df, columns=[column_name])
        else:
            raise ValueError(f"Unsupported encoding method: {encoding_method}")

    def view_column_description(self, column_name: str) -> None:
        column = self.df[column_name]
        print(f"First 5 rows:\n{column.head()}")
        print(f"\nLast 5 rows:\n{column.tail()}")
        print(f"\nValue counts:\n{column.value_counts()}")
        print(f"\nUnique values:\n{column.unique()}")

# Usage example
data_processor = DataProcessor("path/to/your/file.csv")
data_processor.read_data()
data_processor.encode_column("column_name", "categorical")
data_processor.view_column_description("column_name")