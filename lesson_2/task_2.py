import chardet
import json

# Function for get encoding from json file
def coding_function():
    with open("lesson_2/orders.json", "rb") as f:
        return chardet.detect(f.read())["encoding"]

# Function for prepeare information for upload json file
def prepear_json(coding, new_order):
    with open("lesson_2/orders.json", "r", encoding=coding) as f:
        file = json.load(f)
        file["orders"].append(new_order)
        data_base = json.dumps(file)
        data_base = json.loads(str(data_base))
        return data_base

# Function for upload json file
def upgrade_json(data_base):
    with open("lesson_2/orders.json", "w", encoding="utf-8") as file_json :   
        json.dump(data_base, file_json, indent=4)

# Download and show result
def check_result():
    with open("lesson_2/orders.json", "r", encoding=coding) as f:
        file = json.load(f)
        for i in file["orders"]:
            print(i)


###############################################################################################
def write_order_to_json(item, quantity, price, buyer, date):
    global coding   

    coding = coding_function()
    new_order = {"item":item, "quantity": quantity, "price": price, "buyer": buyer, "date":date}
    data_base = prepear_json(coding, new_order)
    upgrade_json(data_base)


write_order_to_json("coffee", 1, 1100, "Mihail", "2022, 10, 02")
write_order_to_json("tea", 10, 1500, "SKolya", "2020, 05, 10")
check_result()