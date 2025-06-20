import pytest
import pandas as pd
from nlp_core.data_utils import load_csv_to_dataframe, calculate_column_mean, filter_dataframe_by_value

# Create a dummy CSV file for testing
@pytest.fixture(scope="module")
def sample_csv(tmp_path_factory):
    csv_content = """col1,col2,col3
1,10.5,A
2,20.0,B
3,15.2,A
4,25.8,C
"""
    file_path = tmp_path_factory.mktemp("data") / "test_data.csv"
    file_path.write_text(csv_content)
    return file_path

def test_load_csv_to_dataframe_success(sample_csv):
    df = load_csv_to_dataframe(sample_csv)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert list(df.columns) == ['col1', 'col2', 'col3']

def test_load_csv_to_dataframe_file_not_found():
    df = load_csv_to_dataframe("non_existent_file.csv")
    assert df is None

def test_calculate_column_mean_success(sample_csv):
    df = load_csv_to_dataframe(sample_csv)
    mean_val = calculate_column_mean(df, 'col2')
    assert mean_val == pytest.approx(17.875)

def test_calculate_column_mean_non_existent_column(sample_csv):
    df = load_csv_to_dataframe(sample_csv)
    mean_val = calculate_column_mean(df, 'non_existent_col')
    assert mean_val is None

def test_calculate_column_mean_non_numeric_column(sample_csv):
    df = load_csv_to_dataframe(sample_csv)
    mean_val = calculate_column_mean(df, 'col3')
    assert mean_val is None

def test_filter_dataframe_by_value_success(sample_csv):
    df = load_csv_to_dataframe(sample_csv)
    filtered_df = filter_dataframe_by_value(df, 'col3', 'A')
    assert isinstance(filtered_df, pd.DataFrame)
    assert len(filtered_df) == 2
    assert all(filtered_df['col3'] == 'A')

def test_filter_dataframe_by_value_non_existent_column(sample_csv):
    df = load_csv_to_dataframe(sample_csv)
    filtered_df = filter_dataframe_by_value(df, 'non_existent_col', 'A')
    assert filtered_df is None

def test_filter_dataframe_by_value_no_match(sample_csv):
    df = load_csv_to_dataframe(sample_csv)
    filtered_df = filter_dataframe_by_value(df, 'col3', 'Z')
    assert isinstance(filtered_df, pd.DataFrame)
    assert filtered_df.empty