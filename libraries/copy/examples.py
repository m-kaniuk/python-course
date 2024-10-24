import copy

# Przykładowy obiekt zagnieżdżony (słownik zawierający listę)
original = {"name": "Jan", "age": 30, "skills": ["Python", "Java", "C++"]}

# Przypisanie obiektu do nowej zmiennej (operator =)
assigned_copy = original

# Tworzenie płytkiej kopii obiektu
shallow_copy = copy.copy(original)

# Tworzenie głębokiej kopii obiektu
deep_copy = copy.deepcopy(original)

# Zmiana wartości w oryginalnym obiekcie
original["name"] = "Adam"
original["skills"].append("JavaScript")

print("Oryginalny obiekt:", original)
print("Przypisanie (operator =):", assigned_copy)
print("Płytka kopia:", shallow_copy)
print("Głęboka kopia:", deep_copy)
