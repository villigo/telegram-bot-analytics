import requests


def update_token(client_id, client_secret, refresh_token):
    """Обновление токена для запросов к API. Возвращает токен"""
    url_token = 'https://accounts.google.com/o/oauth2/token'
    params = {'client_id': client_id, 'client_secret': client_secret,
              'refresh_token': refresh_token, 'grant_type': 'refresh_token'}
    r = requests.post(url_token, data=params)
    return r.json()['access_token']
