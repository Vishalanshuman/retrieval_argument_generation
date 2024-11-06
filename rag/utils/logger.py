import logging
import os
from datetime import datetime

class Logger:

    def __init__(self, log_name="app.log", log_level=logging.INFO):

        log_dir = "logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Set up log file path with timestamp
        log_file = os.path.join(log_dir, f"{datetime.now().strftime('%Y-%m-%d')}_{log_name}")

        # Configure the logger
        logging.basicConfig(
            filename=log_file,
            filemode="a",
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            level=log_level
        )

        self.logger = logging.getLogger(log_name)
        
        # Also log to console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)
        console_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        console_handler.setFormatter(console_formatter)
        
        self.logger.addHandler(console_handler)
    
    def get_logger(self):
        """
        Retrieve the configured logger.
        
        Returns:
            logging.Logger: The configured logger instance.
        """
        return self.logger
