def dodaj_ksiazke(biblioteka):
    try:
        tytul = input("Podaj tytuł książki: ").strip()
        autor = input("Podaj autora książki: ").strip()
        if not tytul or not autor:
            raise ValueError("Tytuł i autor nie mogą być puste.")
        biblioteka.append({"tytul": tytul, "autor": autor})
        print(f"Książka '{tytul}' została dodana.")
    except ValueError as e:
        print(f"Błąd: {e}")

def wyswietl_ksiazki(biblioteka):
    if not biblioteka:
        print("Biblioteka jest pusta.")
        return
    print("\nLista książek w bibliotece:")
    for idx, ksiazka in enumerate(biblioteka, start=1):
        print(f"{idx}. {ksiazka['tytul']} - {ksiazka['autor']}")
    print()

def szukaj_ksiazki(biblioteka):
    try:
        tytul = input("Podaj tytuł książki do wyszukania: ").strip()
        if not tytul:
            raise ValueError("Tytuł nie może być pusty.")
        znalezione = [ksiazka for ksiazka in biblioteka if ksiazka['tytul'].lower() == tytul.lower()]
        if znalezione:
            print("\nZnalezione książki:")
            for ksiazka in znalezione:
                print(f"{ksiazka['tytul']} - {ksiazka['autor']}")
        else:
            print("Nie znaleziono książki o podanym tytule.")
    except ValueError as e:
        print(f"Błąd: {e}")

def usun_ksiazke(biblioteka):
    try:
        tytul = input("Podaj tytuł książki do usunięcia: ").strip()
        if not tytul:
            raise ValueError("Tytuł nie może być pusty.")
        for ksiazka in biblioteka:
            if ksiazka['tytul'].lower() == tytul.lower():
                biblioteka.remove(ksiazka)
                print(f"Książka '{tytul}' została usunięta.")
                return
        print("Nie znaleziono książki o podanym tytule.")
    except ValueError as e:
        print(f"Błąd: {e}")

def main():
    biblioteka = []
    while True:
        print("\nMenu:")
        print("1. Dodaj książkę")
        print("2. Wyświetl książki")
        print("3. Wyszukaj książkę")
        print("4. Usuń książkę")
        print("5. Wyjdź")
        wybor = input("Wybierz opcję (1-5): ").strip()
        
        if wybor == "1":
            dodaj_ksiazke(biblioteka)
        elif wybor == "2":
            wyswietl_ksiazki(biblioteka)
        elif wybor == "3":
            szukaj_ksiazki(biblioteka)
        elif wybor == "4":
            usun_ksiazke(biblioteka)
        elif wybor == "5":
            print("Zamykam program. Do widzenia!")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    main()
