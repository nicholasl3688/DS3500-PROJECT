#tests/test_data_output.py

import pandas as pd

from src import save_data


def test_temporary_path(tmp_path):
    output_path = tmp_path / "clean.csv"


def test_save_data_creates_csv(sample_df, tmp_path):
    output_path = tmp_path / "clean.csv"

    # TODO: Call save_data() and store its return value.
    # TODO: Assert that the returned path is correct.
    # TODO: Read the saved CSV with pandas.
    # TODO: Assert that its row count and column names match sample_df.
    saved_path = save_data(sample_df, output_path)

    assert saved_path == output_path

    df = pd.read_csv(saved_path)

    assert len(df) == len(sample_df)
    assert list(df.columns) == list(sample_df.columns)