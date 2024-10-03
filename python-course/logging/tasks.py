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

""" 
=================================================================================================
Zadanie 2: Logowanie na Konsolę i do Pliku
Skonfiguruj logger, który wysyła komunikaty logowania zarówno do pliku, jak i na konsolę.

1. Utwórz logger.
2. Dodaj FileHandler i StreamHandler do loggera.
3. Ustaw poziomy logowania i formattery dla każdego handlera.
4. Przetestuj logger, logując komunikaty na różnych poziomach.
"""


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
