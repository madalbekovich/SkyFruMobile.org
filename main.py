import requests
import json
import time
import hashlib
from typing import Optional


def get_hash(word):
    hash = hashlib.md5(word.encode('utf-8')).hexdigest()
    return hash

def start_session():
    login = 'api_test_skyfru'
    password = 'api_test_skyfru'
    host = 'https://skyfru.travelshop.aero/bitrix/components/travelshop/ibe.rest/StartSession/'
    hash_text = login + password
    hash = get_hash(hash_text)

    session = requests.Session()
    session.auth = (login, password)

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "login": "api_test_skyfru",
        "password": "api_test_skyfru",
        "currency": "",
        "hash": hash

    }
    response = session.post(url=host, headers=headers, data=json.dumps(data))
    try:
        response.status_code == 200
        body_json = response.json()
        session_token = body_json.get("session_token", "")
        print("Session token: ", session_token)
        return session_token
    except Exception as ex:
        print(f"Damn... there was some error...  :( {ex}", response.status_code)
        return


def get_points(session_token):
    host = "https://skyfru.travelshop.aero/bitrix/components/travelshop/ibe.rest/GetPoints/"
    hash = get_hash(session_token + "Y")
    data = {
        "session_token": session_token,
        "own_route": "Y",
        "hash":hash
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(
        url=host,
        data=json.dumps(data),
        headers=headers,
        timeout=320
    )
    try:
        response.status_code == 200
        print(f"Get points data: \n {response.json()}")
    except Exception as ex:
        print(f"Damn... there was some error...  :( {ex}", response.status_code, hash)
    

def get_optimal_fires(
        session_token: str,
        owrt: str,
        departure_point: str,
        arrival_point: str,
        outbound_date: str,
        adult_count: int,
        outbound_time_range: Optional[str] = None,
        return_time_range: Optional[str] = None,
        child_count: Optional[str] = None,
        infant_count: Optional[str] = None, 
        return_date: Optional[str] = None,
        class_: Optional[str] = None,
        deeplink: Optional[str] = None,
        direct_only: Optional[str] = None,
        promocode: Optional[str] = None,
        date_range: Optional[str] = None,
        price_range: Optional[str] = None,
        cache_usage: Optional[str] = None,
        return_full_names: Optional[str] = None,
        max_count: Optional[str] = None
    ):

    """
    Функция для получения данных о точках маршрута с учетом различных параметров.

    :param session_token: Токен сессии для аутентификации.
    :param owrt: Флаг маршрута (если собственный).
    :param departure_point: Точка отправления.
    :param arrival_point: Точка прибытия.
    :param outbound_date: Дата выезда.
    :param outbound_time_range: Диапазон времени для выезда.
    :param return_date: Дата возвращения.
    :param return_time_range: Диапазон времени для возвращения.
    :param adult_count: Количество взрослых.
    :param child_count: Количество детей.
    :param infant_count: Количество младенцев.
    :param class_: Класс (например, эконом, бизнес и т.д.).
    :param deeplink: Ссылка на ресурс (если есть).
    :param direct_only: Если только прямые рейсы.
    :param promocode: Промокод.
    :param date_range: Диапазон дат.
    :param price_range: Диапазон цен.
    :param cache_usage: Использование кэшированных данных.
    :param return_full_names: Возвращать полные имена.
    :param max_count: Максимальное количество точек маршрута.
    """

    start_time = time.time()
    host = "https://skyfru.travelshop.aero/bitrix/components/travelshop/ibe.rest/GetOptimalFares/"
    
    hash = get_hash(
        f"{session_token}{owrt}{departure_point}{arrival_point}{outbound_date}{adult_count}{return_full_names}"
    )

    data = {
        "session_token": session_token,
        "owrt": owrt,
        "departure_point": departure_point,
        "arrival_point": arrival_point,
        "outbound_date": outbound_date,
        "return_date": return_date,
        "adult_count": adult_count,
        "outbound_time_range": outbound_time_range,
        "return_time_range": return_time_range,
        "child_count": child_count,
        "infant_count": infant_count,
        "class_": class_,
        "deeplink": deeplink,
        "direct_only": direct_only,
        "promocode": promocode,
        "date_range": date_range,
        "price_range": price_range,
        "cache_usage": cache_usage,
        "return_full_names": return_full_names,
        "max_count": max_count,
        "hash": hash
    }
    hash_result = data.get('hash', )
    print("HASH token: ", hash_result)
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(
        url=host,
        data=json.dumps(data),
        headers=headers,
        timeout=320
    )

    try:
        response.status_code == 200
        print(f"Get optimal fares data: \n {json.dumps(response.json(), indent=4, ensure_ascii=False)}")
    except Exception as ex:
        print(f"Damn... there was some error...  :( {ex}", response.status_code, hash)
    finally:
        end_time = time.time()
        result_time = start_time - end_time
        print(f"Время выполнения запроса: {result_time:.5f} sec")

    
if __name__ == "__main__":
    session_token = start_session()
    get_optimal_fires(session_token=session_token, owrt="OW",departure_point="FRU", arrival_point="OSS", outbound_date="27.02.2025", adult_count=1, return_full_names="N")