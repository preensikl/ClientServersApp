from base64 import decode, encode
import chardet


words = {"разработка", "администрирование", "protocol", "standard"}
words_bytes=[]
words_decode=[]
for word in words:
    words_bytes.append(word.encode(encoding="utf-8", errors="replace"))

for obj in words_bytes:
    code_of_obj = chardet.detect(obj)
    words_decode.append(obj.decode(code_of_obj["encoding"]))

print(words_bytes)
print(words_decode)
