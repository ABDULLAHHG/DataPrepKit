import pandas as pd

class DataProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.file_extension = self.file_path.rsplit(".", 1)[-1].lower()
        self.df = None

    def read_data(self) -> None :
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

    def view_dataframe_description(self) -> None:
        print(f"First 5 rows:\n{self.df.head()}")
        print(f"\nLast 5 rows:\n{self.df.tail()}")
        print(f"\nInfo:\n{self.df.info()}")
    
    def show_missing_values(self) -> None:
        print(f"\n{self.df.isna().sum()}")

    def handling_numerical_missing_values(self , col : str , startigay : str) -> None:
        if self.df[col].dtype == "int64":
            if startigay == "mod":
                self.df[col].fillna(self.df[col].mode()[0], inplace = True)
            elif startigay == "mean":
                self.df[col].fillna(self.df[col].mean(), inplace = True)
            elif startigay == "median":
                self.df[col].fillna(self.df[col].median(), inplace = True)

        elif self.df[col].dtype == "float64":
            if startigay == "mod":
                self.df[col].fillna(self.df[col].mode()[0], inplace = True)
            elif startigay == "mean":
                self.df[col].fillna(self.df[col].mean(), inplace = True)
            elif startigay == "median":
                self.df[col].fillna(self.df[col].median(), inplace = True)

    def handle_catigorical_missing_values(self , col : str) -> None:
        self.df[col].fillna(self.df[col].mode()[0], inplace = True)


# Example
data_processor = DataProcessor("netflix_titles.csv")
# Read Dataset
data_processor.read_data()
# View dataframe description
data_processor.view_dataframe_description()
# Show missing values 
data_processor.show_missing_values()
# Handle Missing values 
data_processor.handle_catigorical_missing_values("director")
data_processor.show_missing_values()
