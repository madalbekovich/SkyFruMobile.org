import requests
import hashlib
import time
import json
from typing import Optional
from datetime import date

class ApiClient:
    BASE_URL = "https://skyfru.travelshop.aero/bitrix/components/travelshop/ibe.rest/"

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.session_token = None
        self.session = requests.Session()
        self.session.auth = (login, password)

    def generate_hash(self, text: str) -> str:
        """Generating md5 hash"""
        return hashlib.md5(text.encode('utf-8')).hexdigest()

    def start_session(self) -> Optional[str]:
        """Running session, and receipt token"""
        user = self.login + self.password
        hash_value = self.generate_hash(user)

        data = {
            "login": self.login,
            "password": self.password,
            "currency": "",
            "hash": hash_value

        }
        request = self.session.post(
            url=f"{self.BASE_URL}StartSession/", 
            headers={"Content-Type": "application/json"},
            json=data,
            timeout=30,
        )
        try:
            request.raise_for_status()
            response = request.json()
            self.session_token = response.get("session_token", "")  
            print("Session token: ", self.session_token)
            return self.session_token
        except Exception as ex:
            print(f"Ошибка: {ex}", request.status_code)
            return None
    
    def get_points(self) -> None:
        if not self.session_token:
            print("Token not transferred!")
            return
        
        hash_value = self.generate_hash(self.session_token + "Y")
        data = {
            "session_token": self.session_token,
            "own_route": "Y",
            "hash": hash_value
        }

        request = requests.post(
            url=f"{self.BASE_URL}GetPoints/",
            headers={"Content-Type": "application/json"},
            data=data,
            timeout=30,
        )
        try:
            request.raise_for_status()
            response = request.json()
            print(f"Get points data: \n {response.json()}")
        except Exception as ex:
            print(f"Well, fuck me, it’s busted...  :( {ex} status code {response.status_code}")

    def get_optimal_fares(self, **kwargs) -> Optional[str]:
        """Получение оптимальных тарифов"""
        start_time = time.time()

        if not self.session_token:
            self.start_session()  

        if not self.session_token:
            print("Ошибка: не удалось получить токен")
            return None

        hash_text = (
            f"{self.session_token}"
            f"{kwargs.get('owrt')}"
            f"{kwargs.get('departure_point')}"
            f"{kwargs.get('arrival_point')}"
            f"{kwargs.get('outbound_date')}"
            f"{kwargs.get('return_date', '')}"
            f"{kwargs.get('adult_count')}"
            f"{kwargs.get('child_count')}"
            f"{kwargs.get('infant_count')}"
            "Y"  
        )
        hash_value = self.generate_hash(hash_text)
        # print(f"Сгенерированный хеш: {hash_value}")
        data = {
            "session_token": self.session_token, 
            "owrt": kwargs.get('owrt'),
            "adult_count": kwargs.get('adult_count'),
            "child_count": kwargs.get('child_count'),
            "infant_count": kwargs.get('infant_count'),
            "departure_point": kwargs.get('departure_point'),
            "arrival_point": kwargs.get('arrival_point'),
            "outbound_date": kwargs.get('outbound_date'),
            "return_date": kwargs.get('return_date'),
            "return_full_names": "Y",
            "hash": hash_value
        }
        response = self.session.post(
            url=f"{self.BASE_URL}/GetOptimalFares/",
            headers={"Content-Type": "application/json"},
            json=data,
            timeout=120,
        )

        try:
            response.raise_for_status()
            return response.json()
        except Exception as ex:
            print(f"Ошибка: {ex} status code {response.status_code}")
            return 
        finally:
            end_time = time.time()
            print(f"Время выполнения запроса: {end_time - start_time:.5f} sec")

        
    def add_user(
        self, login: str, email: str = None, password: str = None, confirm_password: str = None,
        last_name: str = None, first_name: str = None, phone: str = None
    ) -> str:
        
        if not self.session_token:
            print("Token not received")
            return
        
        hash_text = f"{self.session_token}{login}{email}{password}{confirm_password}{last_name}{first_name}{phone}"
        hash_value = self.generate_hash(hash_text)

        data = {
            "session_token": self.session_token,
            "login": login,
            "email": email,
            "password": password,
            "confirm_password": confirm_password,
            "last_name": last_name,
            "name": first_name,
            "personal_mobile": phone,
            "hash": hash_value
        }

        response = self.session.post(
            url=f"{self.BASE_URL}AddUser/",
            headers={"Content-Type": "application/json"},
            json=data,
            timeout=120,
        )

        return response.json()

    def authorization_user(
        self, email: str, password: str
    ) -> str:
        hash_text = f"{self.session_token}{email}{password}"
        hash_value = self.generate_hash(hash_text)

        data = {
            "session_token": self.session_token,
            "user_login": email,
            "user_password": password,
            "hash": hash_value
        }
        request = self.session.post(
            url=f"{self.BASE_URL}/AuthorizeUser/",
            headers={"Content-Type": "application/json"},
            json=data,
            timeout=120
        )
        return request.json()