# import hashlib
# from main import get_hash
# import requests
# import json
# from main import start_session

# token = start_session()
# text = f"{token}OWFRUOSS27.02.20251001Y"

# print(f"Строка для хеширования: {text}")

# hash_value = get_hash(text)
# print(f"Хеш: {hash_value}")

# headers = {
#     "Content-Type": "application/json"
# }

# data = {
#     "session_token": token,
#     "owrt": "OW",
#     "adult_count": "1",
#     "child_count": "0",
#     "infant_count": "0",
#     "date_range": "1",
#     "return_full_names": "Y",
#     "departure_point": "FRU",
#     "arrival_point": "OSS",
#     "outbound_date": "27.02.2025",
#     # "return_date": "23.03.2025",
#     "hash": hash_value  
# }
# print(hash_value)

# print(f"Отправляемые данные: {json.dumps(data, indent=4, ensure_ascii=False)}")

# response = requests.post(url="https://skyfru.travelshop.aero/bitrix/components/travelshop/ibe.rest/GetAvailability/", json=data, headers=headers)

# if response.status_code == 200:
#     with open('flights.json', 'w', encoding='utf-8') as f:
#         json.dump(response.json(), f, indent=4, ensure_ascii=False)
# else:
#     print(json.dumps(response.json(), indent=4, ensure_ascii=False))



import hashlib
import requests
import json

def get_hash(text: str) -> str:
    return hashlib.md5(text.encode()).hexdigest()

session_token = "gn702r5um1v1p28dhdu7bt91ve"
login = "Talasbek"
email = "talasbek@example.com"
password = "111111"
last_name = "Иванов"
first_name = "Таласбек"
second_name = "Петров"
birthday = "1990-05-15"
phone = "+996555123456"
doctype = "passport"
doc_cnt = "US"
doc_number = "AB123456"

hash_text = f"{session_token}{login}{email}{password}{password}{last_name}{first_name}{second_name}{birthday}{phone}{doctype}{doc_cnt}{doc_number}"
print("text before hash:", hash_text)

hash_value = get_hash(hash_text)

data = {
    "session_token": session_token,
    "login": login,
    "email": email,
    "password": password,
    "confirm_password": password,
    "last_name": last_name,
    "name": first_name,
    "second_name": second_name,
    "personal_birthday": birthday,
    "personal_mobile": phone,
    "uf_personal_doctype": doctype,
    "uf_personal_doccnt": doc_cnt,
    "uf_personal_docnum": doc_number,
    "hash": hash_value
}

headers = {
    "Content-Type": "application/json"
}

url = "https://skyfru.travelshop.aero/bitrix/components/travelshop/ibe.rest/AddUser/"

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    try:
        print(json.dumps(response.json(), indent=4, ensure_ascii=False))
    except requests.exceptions.JSONDecodeError:
        print("Ответ сервера не является JSON:")
        print(response.text)
else:
    print(f"Ошибка {response.status_code}:")
    print(response.text)