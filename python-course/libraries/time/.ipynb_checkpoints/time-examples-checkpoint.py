import time

# 1. Pomiar czasu wykonania fragmentu kodu
start_time = time.time()

# Przykładowy blok kodu
for i in range(1000000):
    pass  # Symulacja pracy przy użyciu pętli

end_time = time.time()
execution_time = end_time - start_time
print(f"Czas wykonania: {execution_time:.6f} sekund")

# 2. Formatowanie bieżącego czasu
current_time = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
print(f"Bieżący czas: {formatted_time}")

# 3. Wstrzymanie wykonania programu przy użyciu sleep
print("Wstrzymanie wykonania na 3 sekundy...")
time.sleep(3)
print("Kontynuacja wykonania po 3 sekundach")
