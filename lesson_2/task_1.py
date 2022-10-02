import chardet
import re
import csv

#Just prepear lists with infromation
names_list = [r"Изготовитель ОС:.+", r"Название ОС:.+", r"Код продукта:.+", r"Тип системы:.+"]
names_list_del = ["Изготовитель ОС:                  ", "Название ОС:                      ",
    "Код продукта:                     ", "Тип системы:                      " ]
lists = [list("manufacturer_OS_list"), list("name_OS_list"), 
    list("products_code_list"), list("systems_type_list")]
main_data = [["Изготовитель системы", "Название ОС", "Код продукта", "Тип системы"]]
files = ["lesson_2/info_1.txt", "lesson_2/info_1.txt", "lesson_2/info_3.txt"]


# Decoding and get text
def get_text(i):
    with open(i, 'rb') as f_txt:
        decoding = chardet.detect(f_txt.read())["encoding"] 
        f_txt.seek(0)
        text = f_txt.read().decode(decoding)
    return text

# Search, preparation and use "regular"
def get_main_data():
    for i in files:
        text = get_text(i)               
        for el in range(4):
            lists[el] = str(re.findall(names_list[el], text)).replace(names_list_del[el], "").replace(r" \r", "").replace(r"\r", "").replace("['", "").replace("']", "")
            prepeare_data = [[lists[0], lists[1], lists[2], lists[3]]]
        main_data.append(prepeare_data)
    return main_data

# Upload "csv" file
def upload_csv(file, main_data):
    with open(file, "w", encoding="utf-8") as f_csv:
        f_csv_writer = csv.writer(f_csv)
        f_csv_writer.writerows(main_data)


# The main function
def write_to_csv(file):
    def get_data():
        main_data = get_main_data()
        upload_csv(file, main_data)        
    get_data() # Function for homework conditions


write_to_csv("lesson_2/data_base.csv")
