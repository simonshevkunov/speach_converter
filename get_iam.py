import requests
import json
'''
curl -d "{\"yandexPassportOauthToken\":\"<OAuth-token>\"}" "https://iam.api.cloud.yandex.net/iam/v1/tokens"
'''

with open('iam.txt', 'w') as f:
    resp = requests.post(
        f"https://iam.api.cloud.yandex.net/iam/v1/tokens",
        json={
            "yandexPassportOauthToken": 'AQAAAAAB7m1eAATuwYTLOMRWIUi3nLobmWqx1RA'
        })
    res = json.loads(resp.content)
    f.write(res['iamToken'])