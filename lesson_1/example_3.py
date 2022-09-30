words = ['attribute', 'класс', 'функция', 'type']
for word in words:
    try:
        bytes(word, "ASCII")
    except:
        print(word, "- impossible write like bytes type of 'SASCII encoding'")