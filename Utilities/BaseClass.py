import logging

class BaseClass:
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    file_handler = logging.FileHandler('test.log')
    file_handler.setLevel(logging.INFO)

    file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(file_formatter)

    logger.addHandler(file_handler)

    @classmethod
    def log_info(cls, message):
        """Log informational messages."""
        cls.logger.info(message)

    @classmethod
    def log_warning(cls, message):
        """Log warning messages."""
        cls.logger.warning(message)

    @classmethod
    def log_error(cls, message):
        """Log error messages."""
        cls.logger.error(message)

    @classmethod
    def log_exception(cls, message):
        """Log exceptions."""
        cls.logger.exception(message)
