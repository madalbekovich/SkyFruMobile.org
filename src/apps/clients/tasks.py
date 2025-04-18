from celery import shared_task
from apps.helpers.common.service import ApiClient

@shared_task
def send_user_to_api(email, password, first_name, last_name, phone):
    client_api = ApiClient(login="api_test_skyfru", password="api_test_skyfru")
    client_api.start_session()

    if not client_api.session_token:
        return {"error": "Не удалось получить сессию API"}

    response = client_api.add_user(
        email=email,
        password=password,
        confirm_password=password,
        login=first_name,
        last_name=last_name,
        first_name=first_name,
        phone=phone,
    )
    return response
