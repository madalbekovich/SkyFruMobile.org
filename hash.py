# import hashlib
# from main import get_hash
# import requests
# import json
from main import start_session

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

# def start_session():
#     login = 'api_test_skyfru'
#     password = 'api_test_skyfru'
#     host = 'https://skyfru.travelshop.aero/bitrix/components/travelshop/ibe.rest/StartSession/'
#     hash_text = login + password
#     hash = get_hash(hash_text)

#     session = requests.Session()
#     session.auth = (login, password)

#     headers = {
#         "Content-Type": "application/json"
#     }

#     data = {
#         "login": "api_test_skyfru",
#         "password": "api_test_skyfru",
#         "currency": "",
#         "hash": hash

#     }
#     response = session.post(url=host, headers=headers, data=json.dumps(data))
#     try:
#         response.status_code == 200
#         body_json = response.json()
#         session_token = body_json.get("session_token", "")
#         print("Session token: ", session_token)
#         return session_token
#     except Exception as ex:
#         print(f"Damn... there was some error...  :( {ex}", response.status_code)
#         return

# session_token = start_session()
# user_login = "Tala"
# user_password = "111111"

# hash_text = f"{session_token}{user_login}{user_password}"
# # print("text before hash:", hash_text)

# hash_value = get_hash(hash_text)

# data = {
#     "session_token": session_token,
#     "user_login": user_login,
#     "user_password": user_password,
#     "hash": hash_value
# }

# headers = {
#     "Content-Type": "application/json"
# }

# url = "https://skyfru.travelshop.aero/bitrix/components/travelshop/ibe.rest/AuthorizeUser/"

# response = requests.post(url, json=data, headers=headers)
# print(json.dumps(data, indent=4, ensure_ascii=False))

# if response.status_code == 200:
#     try:
#         print(json.dumps(response.json(), indent=4, ensure_ascii=False))
#     except requests.exceptions.JSONDecodeError:
#         print("Ответ сервера не является JSON:")
#         print(response.text)
# else:
#     print(f"Ошибка {response.status_code}:")
#     print(response.text)


# import requests
# import json
# import hashlib


# def get_hash(text):
#     return hashlib.md5(text.encode('utf-8')).hexdigest()

# session_token = start_session()
# user_id = "45"

# passengers = [
#     {
#         "type": "ADT",
#         "gender": "M",
#         "last_name": "Williams",
#         "first_name": "William",
#         "second_name": "Williams",
#         "birthday": "20.01.1985",
#         "doctype": "НП",
#         "docnumber": "444555666",
#         "docexpiration": "30.10.2030"
#     }
# ]

# contacts = [
#     {
#         "ctc_last_name": "Test",
#         "ctc_first_name": "Test",
#         "ctc_phone": "79095674433",
#         "ctc_mail": "test@gmail.com"
#     }
# ]

# hash_text = (
#     session_token +
#     user_id +
#     passengers[0]["type"] +
#     passengers[0]["gender"] +
#     passengers[0]["last_name"] +
#     passengers[0]["first_name"] +
#     passengers[0]["second_name"] +
#     passengers[0]["birthday"] +
#     passengers[0]["doctype"] +
#     passengers[0]["docnumber"] +
#     passengers[0]["docexpiration"] +
#     contacts[0]["ctc_last_name"] +
#     contacts[0]["ctc_first_name"] +
#     contacts[0]["ctc_phone"] +
#     contacts[0]["ctc_mail"]
# )

# hash_value = get_hash(hash_text)

# data = {
#     "session_token": session_token,
#     "user_id": user_id,
#     "passengers": passengers,
#     "contacts": contacts,
#     "hash": hash_value
# }

# headers = {
#     "Content-Type": "application/json"
# }

# url = "https://skyfru.travelshop.aero/bitrix/components/travelshop/ibe.rest/AddUserProfiles/"

# response = requests.post(url, json=data, headers=headers)

# print("Отправленные данные:")
# print(json.dumps(data, indent=4, ensure_ascii=False))

# if response.status_code == 200:
#     try:
#         print("Ответ сервера:")
#         print(json.dumps(response.json(), indent=4, ensure_ascii=False))
#     except requests.exceptions.JSONDecodeError:
#         print("Ответ сервера не является JSON:")
#         print(response.text)
# else:
#     print(f"Ошибка {response.status_code}:")
#     print(response.text)




# session_token = start_session()
# user_id = 4623

# hash_text = f"{session_token}{user_id}"
# # print("text before hash:", hash_text)

# hash_value = get_hash(hash_text)

# data = {
#     "session_token": session_token,
#     "user_id": user_id,
#     "hash": hash_value
# }

# headers = {
#     "Content-Type": "application/json"
# }

# url = "https://skyfru.travelshop.aero/bitrix/components/travelshop/ibe.rest/GetUserProfiles/"

# response = requests.post(url, json=data, headers=headers)
# print(json.dumps(data, indent=4, ensure_ascii=False))

# if response.status_code == 200:
#     try:
#         print(json.dumps(response.json(), indent=4, ensure_ascii=False))
#     except requests.exceptions.JSONDecodeError:
#         print("Ответ сервера не является JSON:")
#         print(response.text)
# else:
#     print(f"Ошибка {response.status_code}:")
#     print(response.text)


#                       AddUser()

# session_token = start_session()
# login = "string"
# email = "user@exampl1e332.com"
# password = "111111"
# last_name = "Иванов"
# first_name = "Таласбек"
# # second_name = "Петров"
# # birthday = "28.05.2005"
# phone = "+996999091423"
# # doctype = "passport"
# # doc_cnt = "US"
# # doc_number = "AB123459"

# # hash_text = f"{session_token}{login}{email}{password}{password}{last_name}{first_name}{second_name}{birthday}{phone}{doc_cnt}{doc_number}"
# hash_text = f"{session_token}{login}{email}{password}{password}{last_name}{first_name}{phone}"

# # print("text before hash:", hash_text)

# hash_value = get_hash(hash_text)

# data = {
#     "session_token": session_token,
#     "login": login,
#     "email": email,
#     "password": password,
#     "confirm_password": password,
#     "last_name": last_name,
#     "name": first_name,
#     # "second_name": second_name,
#     # "personal_birthday": birthday,
#     "personal_mobile": phone,
#     # # "uf_personal_doctype": doctype,
#     # "uf_personal_doccnt": doc_cnt,
#     # "uf_personal_docnum": doc_number,
#     "hash": hash_value
# }

# headers = {
#     "Content-Type": "application/json"
# }

# url = "https://skyfru.travelshop.aero/bitrix/components/travelshop/ibe.rest/AddUser/"

# response = requests.post(url, json=data, headers=headers)
# print(json.dumps(data, indent=4, ensure_ascii=False))

# if response.status_code == 200:
#     try:
#         print(json.dumps(response.json(), indent=4, ensure_ascii=False))
#     except requests.exceptions.JSONDecodeError:
#         print("Ответ сервера не является JSON:")
#         print(response.text)
# else:
#     print(f"Ошибка {response.status_code}:")
#     print(response.text)



session_token = start_session()
user_id = 39
ctc_mail = 'email@gmail.com'
ctc_phone = "+996999091450"
# passengers = []
# hash_text = f"{session_token}{user_login}{user_password}"
hash_text = f"{session_token}{user_id}{ctc_mail}{ctc_phone}"
# print("text before hash:", hash_text)

hash_value = get_hash(hash_text)

data = {
    "session_token": session_token,
    # "user_login": user_login,
    # "user_password": user_password,
    "ctc_mail": ctc_mail,
    "ctc_phone": ctc_phone,
    "user_id": user_id,
    "hash": hash_value
}
print(json.dumps(data, indent=4, ensure_ascii=False))

headers = {
    "Content-Type": "application/json"
}

url = "https://skyfru.travelshop.aero/bitrix/components/travelshop/ibe.rest/CreateOrder/"

response = requests.post(url, json=data, headers=headers)
# print(json.dumps(data, indent=4, ensure_ascii=False))

if response.status_code == 200:
    try:
        print(json.dumps(response.json(), indent=4, ensure_ascii=False), '\n', response.status_code)
    except requests.exceptions.JSONDecodeError:
        print("Ответ сервера не является JSON:")
        print(response.text)
else:
    print(f"Ошибка {response.status_code}:")
    print(response.text)
