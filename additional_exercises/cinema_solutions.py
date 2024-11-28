def wyswietl_miejsca(miejsca):
    print("\nMiejsca w kinie:")
    for rzad, status in enumerate(miejsca, start=1):
        print(f"Miejsce {rzad}: {'Wolne' if status else 'Zajęte'}")
    print()

def zarezerwuj_miejsce(miejsca):
    try:
        rzad = int(input("Podaj numer miejsca do rezerwacji: "))
        if rzad < 1 or rzad > len(miejsca):
            raise ValueError("Nie ma takiego miejsca.")
        if not miejsca[rzad - 1]:
            print("To miejsce jest już zajęte.")
        else:
            miejsca[rzad - 1] = False
            print(f"Miejsce {rzad} zostało zarezerwowane.")
    except ValueError as e:
        print(f"Błąd: {e}")

def main():
    miejsca = [True] * 10  # 10 miejsc, wszystkie wolne
    while True:
        print("\nSystem rezerwacji miejsc w kinie")
        print("1. Wyświetl dostępne miejsca")
        print("2. Zarezerwuj miejsce")
        print("3. Wyjdź")
        wybor = input("Wybierz opcję (1-3): ").strip()

        if wybor == "1":
            wyswietl_miejsca(miejsca)
        elif wybor == "2":
            zarezerwuj_miejsce(miejsca)
        elif wybor == "3":
            print("Zamykam system. Do widzenia!")
            break
        else:
            print("Nieprawidłowy wybór.")

if __name__ == "__main__":
    main()
