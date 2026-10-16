# tests/test_data_validator.py

import pytest

from src import validate_dataframe


def test_validate_dataframe_removes_invalid_ratings(sample_df):
    # TODO: Set the required and numeric column names.
    # TODO: Call validate_dataframe().
    # TODO: Assert that 98 rows remain and all five columns are preserved.
    pass
    req_cols = ["record_id", "name", "rating", "category", "status"]
    numeric_cols = ["rating"]
    df = validate_dataframe(sample_df, req_cols, numeric_cols)

    assert len(df) == 98
    assert list(df.columns) == req_cols 

def test_validate_dataframe_with_missing_column(sample_df):
    # TODO: Set required_columns to include a nonexistent column.
    # TODO: Use pytest.raises(ValueError) around validate_dataframe().
    req_cols = ["record_id", "name", "rating", "category", "status", "ASDASD"]
    numeric_cols = ["rating"]

    with pytest.raises(ValueError):
        validate_dataframe(sample_df, req_cols, numeric_cols)


