import json
import requests
import os

wechat_server = os.environ.get('URL')
bearer = os.environ.get('BEARER')
touser = os.environ.get('TOUSER')


def send_wechat(msg):
    print("Sent wechat...")
    url = 'http://' + wechat_server
    if touser:
        url += '?touser=' + touser
    requests.post(
        url=url,
        headers={"Authorization": bearer, "Content-Type": "application/json"},
        data=json.dumps({
            "app": "mj",
            "msg": msg,
        }),
    )
    print("Wechat sent")


if __name__ == '__main__':
    send_wechat('启动通知')
