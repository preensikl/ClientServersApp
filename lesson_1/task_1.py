words_unicode = {"разработка": "\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430",
"сокет": "\u0441\u043e\u043a\u0435\u0442",
"декоратор": "\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440"
}

for words, unicode in words_unicode.items():
    print(f"word:{type(words)}: {words}\n unicode:{type(unicode)}: {unicode}")