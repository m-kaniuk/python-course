""" 
=================================================================================================
Logging levels
"""

import logging

# Set up basic configuration for logging
logging.basicConfig(level=logging.DEBUG)

# Create log messages
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

""" 
=================================================================================================
Creating handler
"""
logger = logging.getLogger("my_logger")
handler = logging.FileHandler("my_log_file.log")
logger.addHandler(handler)
logger.info("Hello")

""" 
=================================================================================================
Creating formatter
"""
handler = logging.FileHandler("my_log_file_with_formatter")
logger.addHandler(handler)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

logger.info("Hi")

array = []
try:
    array[0] += 1
except Exception as e:
    logger.error(f"An error occured: {e}", exc_info=True)

array = []
try:
    array[0] += 1
except Exception as e:
    logger.error(f"An error occured: {e}")

array = []
try:
    array[0] += 1
except Exception as e:
    logger.exception(f"An error occured: {e}")

""" 
=================================================================================================
Logging to files
"""

import logging
import time
from logging.handlers import TimedRotatingFileHandler

# Tworzenie loggera
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

# Tworzenie TimedRotatingFileHandler
# Parametry: 'app.log' (nazwa pliku), when='M' (nowy plik co minutę), interval=1 (co 1 jednostkę), backupCount=5 (maksymalnie 5 plików archiwalnych)
handler = TimedRotatingFileHandler("app.log", when="M", interval=1, backupCount=5)
handler.setLevel(logging.DEBUG)

# Tworzenie formattera
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

# Dodawanie handlera do loggera
logger.addHandler(handler)

# Przykładowe logi generowane w pętli co 10 sekund
try:
    for i in range(10):
        logger.debug("This is a debug message")
        logger.info("This is an info message")
        logger.warning("This is a warning message")
        logger.error("This is an error message")
        logger.critical("This is a critical message")
        time.sleep(10)  # Poczekaj 10 sekund przed wygenerowaniem kolejnych logów
except KeyboardInterrupt:
    print("Logging interrupted.")
