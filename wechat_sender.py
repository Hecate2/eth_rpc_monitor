import json
import requests
import os

wechat_server = os.environ.get('URL')
bearer = os.environ.get('BEARER')


def send_wechat(msg):
    print("Sent wechat...")
    requests.post(
        url='http://' + wechat_server,
        headers={"Authorization": bearer, "Content-Type": "application/json"},
        data=json.dumps({
            "app": "mj",
            "msg": msg,
        }),
    )
    print("Wechat sent")


if __name__ == '__main__':
    send_wechat('启动通知')
