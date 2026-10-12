import argparse
import logging
import sys
from pathlib import Path
from src import (
    create_cleaning_report,
    load_data,
    process_data,
    save_data,
    setup_logging,
    validate_dataframe,
    validate_input,
)

logger = logging.getLogger(__name__)



def parse_arguments():
# Parse command-line arguments.
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        "-i",
        required=True,
        help="Path to input file"
    )
    parser.add_argument(
        "--config",
        "-c",
        required=True,
        help="Accepts path to the YAML configuration file"
    )
    parser.add_argument(
        "--output",
        "-o",
        required=True,
        help="Path to output file"
    )
    
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Enable verbose logging"
    )

    return parser.parse_args()




def main():
    # """Main pipeline function."""
    args = parse_arguments()
    setup_logging(args.verbose)
    logger.debug(f"Args parsed: input={args.input}, output={args.output}")

    
    if not validate_input(args.input):
        sys.exit(1)
    if not validate_input(args.config):
        sys.exit(1)
    try:
        data = load_data(args.input)
        config = load_data(args.config)
    except ValueError:
        sys.exit(1)

    required_columns = config["validation"]["required_columns"]
    numeric_columns = config["validation"]["numeric_columns"]
    rows_before = len(data)
    try:
        data = validate_dataframe(data, required_columns, numeric_columns)
    except ValueError:
        sys.exit(1)
    logger.info(f"Validation complete: {rows_before} -> {len(data)} rows")

    og_copy = data.copy()
    try:
        data = process_data(data, config)
    except ValueError:
        sys.exit(1)

    report = create_cleaning_report(og_copy, data)
    logger.info(f"Processing complete: {report['rows_before']} -> {report['rows_after']} rows")

    save_data(data, args.output)
    logger.info(f"Saved cleaned data to {args.output}")

    print(report)








if __name__ == "__main__":
    main()