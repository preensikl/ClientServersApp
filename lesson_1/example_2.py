import sys

words = ["class", "function", "method"]
for code in words:
    code = f"b'{code}'"
    code = eval(code)
    print(type(code), code, sys.getsizeof(code), "bytes")
