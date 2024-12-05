x = 10

y = 1

try:
    result = x / y
except ZeroDivisionError:
    print("Dzielenie przez 0")
else:
    print("result: {y}")
finally:
    print("Koniec programu")
