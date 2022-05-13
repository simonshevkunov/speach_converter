import requests
import json
import time

last_time = 0
while True:
    if time.time() - last_time > 3600:
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

        last_time = time.time()

    time.sleep(5)