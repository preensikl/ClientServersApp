import chardet
text = []

with open("text.txt", "w", encoding="utf-8") as f:
    f.write("сетевое программирование\n" "сокет\n" "декоратор")    

def cheker(obj):
    with open(obj, 'rb') as f:
        text = f.read()
    encoding_type = chardet.detect(text)["encoding"]

    with open(obj, "r", encoding=encoding_type) as f:
        print(f.read())
    
    
cheker("text.txt")