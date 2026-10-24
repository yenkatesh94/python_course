"""Logging records useful messages while a program runs.
Different log levels distinguish debugging details, normal events, and warnings.
"""

# Topic 35: Logging

import logging


def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)s: %(message)s",
    )
    logger = logging.getLogger(__name__)

    logger.debug("Detailed information useful while developing.")
    logger.info("The program is running.")
    logger.warning("This is a warning example.")


if __name__ == "__main__":
    main()
