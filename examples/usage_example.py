import os
import pandas as pd
from nlp_core import load_csv_to_dataframe, calculate_column_mean, filter_dataframe_by_value

# Create a dummy CSV file for demonstration
current_dir = os.path.dirname(__file__)
dummy_csv_path = os.path.join(current_dir, "sample_data.csv")

csv_content = """Name,Age,City,Score
Alice,30,New York,85
Bob,24,London,92
Charlie,35,New York,78
David,29,Paris,95
Eve,22,London,88
"""
with open(dummy_csv_path, "w") as f:
    f.write(csv_content)

print(f"Created dummy CSV at: {dummy_csv_path}\n")

# --- Usage of the library functions ---

# Load a CSV file
df = load_csv_to_dataframe(dummy_csv_path)

if df is not None:
    print("\nOriginal DataFrame:")
    print(df)

    # Calculate the mean of a numeric column
    mean_age = calculate_column_mean(df, 'Age')
    print(f"\nMean Age: {mean_age}")

    mean_score = calculate_column_mean(df, 'Score')
    print(f"Mean Score: {mean_score}")

    # Try to calculate mean of a non-numeric column
    calculate_column_mean(df, 'Name')

    # Filter the DataFrame
    filtered_df_ny = filter_dataframe_by_value(df, 'City', 'New York')
    if filtered_df_ny is not None:
        print("\nFiltered by City == 'New York':")
        print(filtered_df_ny)

    filtered_df_london = filter_dataframe_by_value(df, 'City', 'London')
    if filtered_df_london is not None:
        print("\nFiltered by City == 'London':")
        print(filtered_df_london)

    # Clean up the dummy CSV
    os.remove(dummy_csv_path)
    print(f"\nRemoved dummy CSV: {dummy_csv_path}")

else:
    print("Could not proceed with operations as DataFrame loading failed.")