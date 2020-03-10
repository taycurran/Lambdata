"""
Basic DataFrame Summary Functions
"""
import pandas as pd

TEST_DF = pd.read_csv('train.csv')

class TrashPanda():

    def __init__(self, df):
        self.df = df


    def cardinality_report(self, df=TEST_DF):
        """
        Takes a dataframe and returns a report on the cardinality
        of categorical columns within the dataframe
        Params:
            df (pandas DataFrame)
        
        Returns:
            A series of 5 Print Statements for each Categorical Column
            identified in the dataframe separated by a newline
        """
        # Get only categorical features from DF
        df = self.df
        columns = df.describe(exclude='number').columns
        # Evaluate cardinality qualities for each feature
        for col in columns:
            print(f"COLUMN: {col}")
            print(f"nUnique: {df[col].nunique()}")
            print(f"Perc Uniq: {df[col].nunique() / df.shape[0]}")
            print("TOP 5")
            print(df[col].value_counts().nlargest(5))
            print('\n')

    # def reduce_uniques(self, df, column_threshold_dict):
    #     """Takes in a dataframe and a dictionary consisting
    #     of column name : value count threshold returns the original
    #     dataframe"""
    #     for key, value in column_threshold_dict.items():
    #             counts = self.df[key].value_counts()
    #             others = set(counts[counts < value].index)
    #             self.df[key] = self.df[key].replace(list(others), 'Others')
    #             return self.df


if __name__ == "__main__":
    tp = TrashPanda(TEST_DF)
    print(tp.cardinality_report())
 


# def check_facts(df):
#     """
#     Checks basic facts about an entire dataframe.
#     Returns series of print statements.
#     """
#     print(f"Shape: {df.shape}")
#     print(f"PercNull: {df.isna().sum().sum()/df.size}")



# # TODO: Make Funct work for Multiple Datatypes
#  def check_mask(df, target, method='contains'):

#     if target == 

#     for feature in df.columns:
        
#         if method == 'exact':
#             condition = df[feature] == (target)
#         if method == 'isin':
#             condition = df[feature].str.isin(target)
#         if method == 'contains':
#             condition = df[feature].str.contains(target)
#         else:
#             except("method must be 'exact', 'isin', or 'contains'")
    
#         print(feature)
#         print(condition.sum())
#         print()


# def one_hot_encoder(df, column_list):
#     """Takes in a dataframe and a list of columns
#     for pre-processing via one hot encoding returns
#     a dataframe of one hot encoded values"""
#     df_to_encode = df[column_list]
#     df = pd.get_dummies(df_to_encode)
#     return df

# def reduce_uniques(df, column_threshold_dict):
#     """Takes in a dataframe and a dictionary consisting
#     of column name : value count threshold returns the original
#     dataframe"""
#     for key, value in column_threshold_dict.items():
#             counts = df[key].value_counts()
#             others = set(counts[counts < value].index)
#             df[key] = df[key].replace(list(others), 'Others')
#             return df

# def reduce_uniques(self, df, column_threshold_dict):
#     """Takes in a dataframe and a dictionary consisting
#     of column name : value count threshold returns the original
#     dataframe"""
#     for key, value in column_threshold_dict.items():
#             counts = self.df[key].value_counts()
#             others = set(counts[counts < value].index)
#             self.df[key] = self.df[key].replace(list(others), 'Others')
#             return self.df

