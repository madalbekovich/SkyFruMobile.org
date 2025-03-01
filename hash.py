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
from main import get_hash
import requests
import json
from main import start_session

token = start_session()
text = f"{token}test123test123DoeJohnjohn.doe@example.com"

print(f"Строка для хеширования: {text}")

hash_value = get_hash(text)
print(f"Хеш: {hash_value}")

headers = {
    "Content-Type": "application/json"
}

data = {
    "session_token": token,
    "password": "test123",
    "confirm_password": "test123",
    "last_name": "Doe",
    "name": "John",
    "email": "john.doe@example.com",
    # "return_date": "23.03.2025",
    "hash": hash_value  
}
print(hash_value)

print(f"Отправляемые данные: {json.dumps(data, indent=4, ensure_ascii=False)}")

response = requests.post(url="https://skyfru.travelshop.aero/bitrix/components/travelshop/ibe.rest/GetAvailability/", json=data, headers=headers)

if response.status_code == 200:
    with open('flights.json', 'w', encoding='utf-8') as f:
        json.dump(response.json(), f, indent=4, ensure_ascii=False)
else:
    print(response.status_code)
