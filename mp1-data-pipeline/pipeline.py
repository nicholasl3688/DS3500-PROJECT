import argparse
import logging
import sys
from pathlib import Path

logger = logging.getLogger(__name__)

def setup_logging(verbose=False):
# configure looping for te pipeline
    if verbose==False:
        logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)-8s %(message)s",
        datefmt="%H:%M:%S"
        )
    else:
        logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)-8s %(message)s",
        datefmt="%H:%M:%S"
        )

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
        "--output",
        "-o",
        required=True,
        help="Path to output file"
    )
    parser.add_argument(
        "--format",
        required=False,
        choices=["csv", "json"],
        default="csv",
        help="Output format, 'csv' or 'json', default is csv"
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Enable verbose logging"
    )

    return parser.parse_args()


def validate_input(filepath):
    # """Check whether the input path exists and is a file."""
    p = Path(filepath)
    if not p.is_file():
        logger.error(f"Input file not found: {filepath}")
        return False
    else:
        logger.info(f"Input file validated: {filepath}")
        return True




def main():
    # """Main pipeline function."""
    args = parse_arguments()
    setup_logging(args.verbose)
    logger.debug(f"Args parsed: input={args.input}, output={args.output}, format={args.format}")

    valid = validate_input(args.input)
    if not valid:
        sys.exit(1)




if __name__ == "__main__":
    main()