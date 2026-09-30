import logging
import pandas as pd


logger = logging.getLogger(__name__)

def remove_duplicates(df):
    """Remove duplicate rows."""
    before = len(df)
    new = df.drop_duplicates()
    logger.debug(f"Removed {before - len(new)} duplicate rows")
    return new


def handle_missing(df, axis="rows"):
    """Drop rows or columns containing missing values."""
    if axis == "rows":
        rows_dropped = df.dropna()
        logger.debug(f"Dropped {len(df) - len(rows_dropped)} rows")
        return rows_dropped
    elif axis == "columns":
        cols_dropped = df.dropna(axis=1)
        logger.debug(f"Dropped {len(df.columns) - len(df.col_dropped)} columns")
        return cols_dropped
    else:
        logger.error(f"Error, unsupported axis {axis}")
        raise ValueError



def remove_outliers(df, columns, method, threshold):
    """Remove outliers from the specified numeric columns."""
    


def process_data(df, config):
    """Apply the processing steps enabled in the configuration."""
    pass


def create_cleaning_report(df_before, df_after):
    """Return a dictionary summarizing the cleaning results."""
    pass