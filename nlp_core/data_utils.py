import pandas as pd

def load_csv_to_dataframe(filepath):
    """
    Loads a CSV file into a pandas DataFrame.

    Args:
        filepath (str): The path to the CSV file.

    Returns:
        pandas.DataFrame: The loaded DataFrame.
    """
    try:
        df = pd.read_csv(filepath)
        print(f"Successfully loaded {filepath} into a DataFrame.")
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except Exception as e:
        print(f"An error occurred while loading the CSV: {e}")
        return None

def calculate_column_mean(dataframe, column_name):
    """
    Calculates the mean of a specified numeric column in a pandas DataFrame.

    Args:
        dataframe (pandas.DataFrame): The input DataFrame.
        column_name (str): The name of the column to calculate the mean for.

    Returns:
        float or None: The mean of the column, or None if the column is not found
                       or not numeric.
    """
    if dataframe is None:
        return None
    if column_name not in dataframe.columns:
        print(f"Error: Column '{column_name}' not found in DataFrame.")
        return None
    if not pd.api.types.is_numeric_dtype(dataframe[column_name]):
        print(f"Error: Column '{column_name}' is not numeric.")
        return None
    
    mean_value = dataframe[column_name].mean()
    print(f"Mean of column '{column_name}': {mean_value}")
    return mean_value

def filter_dataframe_by_value(dataframe, column_name, value):
    """
    Filters a DataFrame based on a specific value in a given column.

    Args:
        dataframe (pandas.DataFrame): The input DataFrame.
        column_name (str): The name of the column to filter by.
        value: The value to filter for.

    Returns:
        pandas.DataFrame or None: The filtered DataFrame, or None if an error occurs.
    """
    if dataframe is None:
        return None
    if column_name not in dataframe.columns:
        print(f"Error: Column '{column_name}' not found for filtering.")
        return None
    
    filtered_df = dataframe[dataframe[column_name] == value]
    print(f"Filtered DataFrame for '{column_name}' == '{value}'.")
    return filtered_df