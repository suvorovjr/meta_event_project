from common.schemas import PagesResponseModel


def fetch(method: str, url: str, params: dict) -> dict:
    """
    Функция для отправки POST и GET запросов
    """

    if method == 'GET':
        response = requests.get(url=url, params=params)
        return response.json()
    elif method == 'POST':
        response = requests.post(url=url, params=params)
        return response.json()


def get_facebook_pages(access_token: str) -> PagesResponseModel:
    """
    Функция для получения страниц, к которым имеем доступ по API
    """

    method = 'GET'
    url = f'https://graph.facebook.com/v20.0/me/accounts'
    params = {'access_token': access_token}
    response = fetch(method=method, url=url, params=params)
    pages = PagesResponseModel(**response)
    return pages
