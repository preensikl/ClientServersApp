import code
import chardet
import yaml

def unload():
    info = {
        "1€" : ["orange", "apple"],
        "2€" : 138,
        "3€" : {"name": "Misha", "hobby": "sport"}
    }

    with open("file.yaml", "w", encoding="utf-8") as f:
        yaml.dump(info, f, default_flow_style=True, allow_unicode=True)

def dowanload():
    with open("lesson_2/file.yaml", "rb",) as f:
        f_read = f.read()
        coding = chardet.detect(f_read)["encoding"]
        f.seek(0)
        info_decode = f_read.decode(coding)
        print(info_decode)

unload()
dowanload()