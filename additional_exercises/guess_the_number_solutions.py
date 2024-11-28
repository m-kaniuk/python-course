import random

def zgadnij_liczbe():
    liczba_do_zgadniecia = random.randint(1, 100)
    maks_proby = 10
    proby = 0

    print("Witaj w grze 'Zgadnij liczbę'!")
    print("Zgadnij liczbę z zakresu od 1 do 100. Masz 10 prób.")

    while proby < maks_proby:
        try:
            strzal = int(input(f"Próba {proby + 1}/{maks_proby}. Podaj liczbę: "))
            if strzal < 1 or strzal > 100:
                raise ValueError("Liczba musi być w zakresie od 1 do 100.")

            proby += 1

            if strzal == liczba_do_zgadniecia:
                print(f"Gratulacje! Zgadłeś liczbę {liczba_do_zgadniecia} w {proby} próbach.")
                break
            elif strzal < liczba_do_zgadniecia:
                print("Za mało!")
            else:
                print("Za dużo!")
        except ValueError as e:
            print(f"Błąd: {e}")

    else:
        print(f"Przegrałeś! Prawidłowa liczba to {liczba_do_zgadniecia}.")

if __name__ == "__main__":
    zgadnij_liczbe()
