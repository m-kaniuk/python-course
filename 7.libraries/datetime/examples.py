from datetime import datetime, timedelta

# 1. Wyświetlenie bieżącej daty i czasu
now = datetime.now()
print("Bieżąca data i czas:", now)

# 2. Formatowanie daty i czasu jako ciąg znaków
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Sformatowana data i czas:", formatted_date)

# 3. Obliczenie przyszłej daty poprzez dodanie przesunięcia czasowego
days_to_add = 10
future_date = now + timedelta(days=days_to_add)
print(f"Data i czas po {days_to_add} dniach:", future_date)

# Dodatkowe: Parsowanie ciągu znaków reprezentującego datę do obiektu datetime
date_string = "2024-08-05 12:30:00"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Sparsowana data i czas:", parsed_date)
