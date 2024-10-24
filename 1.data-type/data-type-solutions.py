# Zadanie 1
# Napisz program w Pythonie, który sprawdzi typ zmiennej.
var = 5
print(type(var))

# Zadanie 2
# Napisz program w Pythonie, który przekonwertuje ciąg znaków na liczbę całkowitą.
string_num = "123"
int_num = int(string_num)
print(int_num)

# Zadanie 3
# Napisz program w Pythonie, który przekonwertuje liczbę całkowitą na ciąg znaków.
int_num = 123
string_num = str(int_num)
print(string_num)

# Zadanie 4
# Napisz program w Pythonie, który doda dwie liczby podane przez użytkownika.
num1 = float(input("Podaj pierwszą liczbę: "))
num2 = float(input("Podaj drugą liczbę: "))
print(num1 + num2)

# Zadanie 5
# Napisz program w Pythonie, który sprawdzi, czy podana liczba jest liczbą całkowitą, czy zmiennoprzecinkową.
num = 4.5
if isinstance(num, int):
    print("Liczba całkowita")
elif isinstance(num, float):
    print("Liczba zmiennoprzecinkowa")

# Zadanie 6
# Napisz program w Pythonie, który sprawdzi, czy ciąg znaków jest numeryczny.
string = "123"
print(string.isnumeric())

# Zadanie 7
# Napisz program w Pythonie, który sprawdzi, czy zmienna jest określonego typu.
var = "Hello"
if isinstance(var, str):
    print("To jest ciąg znaków")

# Zadanie 8
# Napisz program w Pythonie, który przekonwertuje listę na krotkę.
list_num = [1, 2, 3]
tuple_num = tuple(list_num)
print(tuple_num)

# Zadanie 9
# Napisz program w Pythonie, który przekonwertuje krotkę na listę.
tuple_num = (1, 2, 3)
list_num = list(tuple_num)
print(list_num)

# Zadanie 10
# Napisz program w Pythonie, który sprawdzi, czy wartość istnieje na liście.
list_num = [1, 2, 3]
print(2 in list_num)

# Zadanie 11
# Napisz program w Pythonie, który sprawdzi, czy klucz istnieje w słowniku.
dict_num = {'a': 1, 'b': 2}
print('a' in dict_num)

# Zadanie 12
# Napisz program w Pythonie, który doda nową parę klucz-wartość do słownika.
dict_num = {'a': 1, 'b': 2}
dict_num['c'] = 3
print(dict_num)

# Zadanie 13
# Napisz program w Pythonie, który usunie klucz ze słownika.
dict_num = {'a': 1, 'b': 2}
dict_num.pop('a')
print(dict_num)

# Zadanie 14
# Napisz program w Pythonie, który połączy dwa słowniki.
dict1 = {'a': 1}
dict2 = {'b': 2}
dict1.update(dict2)
print(dict1)

# Zadanie 15
# Napisz program w Pythonie, który utworzy zbiór i doda do niego elementy.
set_num = {1, 2, 3}
set_num.add(4)
print(set_num)

# Zadanie 16
# Napisz program w Pythonie, który usunie element ze zbioru.
set_num = {1, 2, 3}
set_num.remove(2)
print(set_num)

# Zadanie 17
# Napisz program w Pythonie, który sprawdzi, czy wartość istnieje w zbiorze.
set_num = {1, 2, 3}
print(2 in set_num)

# Zadanie 18
# Napisz program w Pythonie, który utworzy listę słowników.
list_of_dicts = [{'a': 1}, {'b': 2}]
print(list_of_dicts)

# Zadanie 19
# Napisz program w Pythonie, który utworzy słownik list.
dict_of_lists = {'numbers': [1, 2, 3], 'letters': ['a', 'b', 'c']}
print(dict_of_lists)

# Zadanie 20
# Napisz program w Pythonie, który przeiteruje przez słownik i wydrukuje każdą parę klucz-wartość.
dict_num = {'a': 1, 'b': 2}
for key, value in dict_num.items():
    print(key, value)
