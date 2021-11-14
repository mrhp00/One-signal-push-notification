import requests
import json


def view():
    header = {"Content-Type": "application/json; charset=utf-8",
              "Authorization": "YOU AUTHORIZATION CODE HERE"}

    payload = {"app_id": "YOUR APP ID HERE",
               "included_segments": ["Subscribed Users"],
               "contents": {"en": "English Message"}}

    req = requests.post("https://onesignal.com/api/v1/notifications", headers=header, data=json.dumps(payload))
    print(req.status_code, req.reason)


view()
