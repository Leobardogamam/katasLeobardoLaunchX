cadena = "The highest temperature on Mars is about 30 C"

for item in cadena.split():
    print(item)
    if item.isnumeric():
        print(item)
