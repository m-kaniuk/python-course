def dodaj(a, b):
    return a + b

def odejmij(a, b):
    return a - b

def pomnoz(a, b):
    return a * b

def podziel(a, b):
    if b == 0:
        raise ZeroDivisionError("Nie można dzielić przez zero.")
    return a / b

def main():
    while True:
        print("\nKalkulator")
        print("1. Dodawanie")
        print("2. Odejmowanie")
        print("3. Mnożenie")
        print("4. Dzielenie")
        print("5. Wyjdź")
        wybor = input("Wybierz operację (1-5): ").strip()
        
        if wybor == "5":
            print("Zamykam kalkulator. Do widzenia!")
            break

        try:
            a = float(input("Podaj pierwszą liczbę: "))
            b = float(input("Podaj drugą liczbę: "))
            if wybor == "1":
                print(f"Wynik: {dodaj(a, b)}")
            elif wybor == "2":
                print(f"Wynik: {odejmij(a, b)}")
            elif wybor == "3":
                print(f"Wynik: {pomnoz(a, b)}")
            elif wybor == "4":
                print(f"Wynik: {podziel(a, b)}")
            else:
                print("Nieprawidłowy wybór.")
        except ValueError:
            print("Błąd: Wprowadź poprawną liczbę.")
        except ZeroDivisionError as e:
            print(f"Błąd: {e}")

if __name__ == "__main__":
    main()
