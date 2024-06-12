class DataframeMethods:
    '''
    Class that hosts different manipulations to dataframes that may be needed to simplify the dataframe.
    '''
    def __init__(self, stock: str, df):
        self.stock = stock
        self.df = df

    def rename_columns(self):
        (self.df).rename(columns={"Close Close price adjusted for splits.": "Close", "Adj Close Adjusted close price adjusted for splits and dividend and/or capital gain distributions." : "Adj Close"}, inplace=True)


    def export_to_csv(self):
        (self.df).to_csv(self.stock + "_stock.csv")
