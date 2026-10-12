# MP1 Data Pipeline

This pipeline cleans a CSV file using settings from a YAML config file instead of hard-coded values. pipeline.py reads the command-line arguments, checks that the input and config files exist, and loads both. The data is then validated (required columns must exist, and bad values in numeric columns are removed), cleaned (duplicates, missing values, and outliers, in that order), and saved as a new CSV, with a cleaning report printed at the end. To use it on a different dataset, you change the file paths and the column names in config/config.yaml, not the code. The code lives in src/: data_loaders.py reads CSV, JSON, and YAML files; data_validator.py checks columns and numeric values; data_processor.py removes duplicates, missing values, and outliers and builds the cleaning report; data_output.py saves the cleaned CSV; and utils.py holds the logging setup and file-path checks. Any problem, such as a missing file, an unsupported file type, a bad config value, or a missing required column, is logged and the pipeline exits with status code 1.

## Run it

pip install -r requirements.txt
python pipeline.py --input fixtures/sample_data.csv --output output/clean.csv --config config/config.yaml --verbose

## Output

15:26:02 DEBUG    __main__ — Args parsed: input=fixtures/sample_data.csv, output=output/clean.csv
15:26:02 INFO     src.utils — Input file validated: fixtures/sample_data.csv
15:26:02 INFO     src.utils — Input file validated: config/config.yaml
15:26:02 INFO     src.data_loaders — Loaded file: fixtures\sample_data.csv, DF length: 100
15:26:02 INFO     src.data_loaders — Loaded file: config\config.yaml
15:26:02 WARNING  src.data_validator — Removed 2 rows with invalid values in rating
15:26:02 DEBUG    src.data_validator — Validation: 100 -> 98 rows (2 removed)
15:26:02 INFO     __main__ — Validation complete: 100 -> 98 rows
15:26:02 DEBUG    src.data_processor — Removed 2 duplicate rows
15:26:02 DEBUG    src.data_processor — Dropped 2 rows
15:26:02 DEBUG    src.data_processor — rating: method=iqr, threshold=1.5, lower=43.625, upper=106.625, removed=2
15:26:02 INFO     __main__ — Processing complete: 98 -> 92 rows
15:26:02 DEBUG    src.data_output — 92 rows saved at path: output\clean.csv
15:26:02 INFO     __main__ — Saved cleaned data to output/clean.csv
{'rows_before': 98, 'rows_after': 92, 'rows_removed': 6, 'columns_before': 5, 'columns_after': 5, 'columns_removed': 0}
