""" 
=================================================================================================
Zadanie 1: Podstawowe Logowanie do Pliku
Skonfiguruj logger, który zapisuje komunikaty logowania do pliku.

1. Utwórz logger.
2. Skonfiguruj FileHandler do zapisywania logów do pliku basic_log.log.
3. Ustaw poziom logowania na DEBUG.
4. Zdefiniuj prosty formatter.
5. Przetestuj logger, logując komunikaty na różnych poziomach (DEBUG, INFO, WARNING, ERROR, CRITICAL).
"""

import logging

# Tworzenie loggera
logger = logging.getLogger("basic_logger")
logger.setLevel(logging.DEBUG)

# Tworzenie FileHandler
file_handler = logging.FileHandler("basic_log.log")
file_handler.setLevel(logging.DEBUG)

# Tworzenie formattera
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Dodanie handlera do loggera
logger.addHandler(file_handler)

# Przykładowe komunikaty logowania
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")


""" 
=================================================================================================
Zadanie 2: Logowanie na Konsolę i do Pliku
Skonfiguruj logger, który wysyła komunikaty logowania zarówno do pliku, jak i na konsolę.

1. Utwórz logger.
2. Dodaj FileHandler i StreamHandler do loggera.
3. Ustaw poziomy logowania i formattery dla każdego handlera.
4. Przetestuj logger, logując komunikaty na różnych poziomach.
"""

import logging

# Tworzenie loggera
logger = logging.getLogger("console_file_logger")
logger.setLevel(logging.DEBUG)

# Tworzenie FileHandler
file_handler = logging.FileHandler("console_file_log.log")
file_handler.setLevel(logging.DEBUG)

# Tworzenie StreamHandler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Tworzenie formattera
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Dodanie handlerów do loggera
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Przykładowe komunikaty logowania
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")


""" 
=================================================================================================
Zadanie 3: Tworzenie Własnego Formattera
Cel: Utwórz własny formatter, który dodaje niestandardowe pole do komunikatów logowania.

Hint: [Atrybuty formattera](https://docs.python.org/3/library/logging.html#logrecord-attributes)

1. Utwórz logger.
2. Utwórz własną klasę formattera, która dodaje niestandardowe pole do komunikatów logowania.
3. Dodaj handler z własnym formatterem do loggera.
4. Przetestuj logger, logując komunikaty na różnych poziomach.
"""

import logging


class CustomFormatter(logging.Formatter):
    def format(self, record):
        record.custom_field = "Custom Value"
        return super().format(record)


# Tworzenie loggera
logger = logging.getLogger("custom_formatter_logger")
logger.setLevel(logging.DEBUG)

# Tworzenie handlera
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)

# Tworzenie własnego formattera
custom_formatter = CustomFormatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(custom_field)s"
)
handler.setFormatter(custom_formatter)

# Dodanie handlera do loggera
logger.addHandler(handler)

# Przykładowe komunikaty logowania
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")

"""
=================================================================================================
Zadanie 4: Logowanie na Konsolę z Różnymi Poziomami Logowania
Skonfiguruj logger, który wysyła komunikaty logowania na konsolę, ale z różnymi handlerami dla różnych poziomów logowania.

1. Utwórz logger.
2. Dodaj dwa StreamHandler:
3. Jeden do obsługi logów na poziomie DEBUG i wyższych.
4. Drugi do obsługi logów na poziomie ERROR i wyższych.
5. Ustaw różne formattery dla obu handlerów.
6. Przetestuj logger, logując komunikaty na różnych poziomach.
"""

import logging

# Tworzenie loggera
logger = logging.getLogger("multi_stream_logger")
logger.setLevel(logging.DEBUG)

# Tworzenie handlerów
debug_handler = logging.StreamHandler()
error_handler = logging.StreamHandler()

# Ustawianie poziomów logowania dla handlerów
debug_handler.setLevel(logging.DEBUG)
error_handler.setLevel(logging.ERROR)

# Tworzenie formatterów
debug_formatter = logging.Formatter("%(asctime)s - %(name)s - DEBUG - %(message)s")
error_formatter = logging.Formatter("%(asctime)s - %(name)s - ERROR - %(message)s")

# Przypisanie formatterów do handlerów
debug_handler.setFormatter(debug_formatter)
error_handler.setFormatter(error_formatter)

# Dodanie handlerów do loggera
logger.addHandler(debug_handler)
logger.addHandler(error_handler)

# Przykładowe komunikaty logowania
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")

""" 
=================================================================================================
Zadanie 5: Logowanie do Oddzielnych Plików na Podstawie Poziomu Logowania
Skonfiguruj logger, który zapisuje komunikaty logowania do różnych plików w zależności od poziomu logowania.


1. Utwórz logger.
2. Dodaj dwa FileHandler:
3. Jeden do zapisywania logów na poziomie INFO i wyższych do pliku info.log.
4. Drugi do zapisywania logów na poziomie ERROR i wyższych do pliku error.log.
5. Ustaw formattery dla obu handlerów.
6. Przetestuj logger, logując komunikaty na różnych poziomach.
"""

import logging

# Tworzenie loggera
logger = logging.getLogger("file_logger")
logger.setLevel(logging.DEBUG)

# Tworzenie handlerów
info_handler = logging.FileHandler("info.log")
error_handler = logging.FileHandler("error.log")

# Ustawianie poziomów logowania dla handlerów
info_handler.setLevel(logging.INFO)
error_handler.setLevel(logging.ERROR)

# Tworzenie formatterów
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
info_handler.setFormatter(formatter)
error_handler.setFormatter(formatter)

# Dodanie handlerów do loggera
logger.addHandler(info_handler)
logger.addHandler(error_handler)

# Przykładowe komunikaty logowania
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
