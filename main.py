# import json
#
# import requests
#
# header = {"Content-Type": "application/json; charset=utf-8",
#           "Authorization": "Basic MjgwNzUwOTItOGIxYi00MDZmLThlZDMtNDI5ZTlhOGZhYzAw"}
#
# payload = {"app_id": "f6cc14cd-b352-47a6-b352-23fcf3731f75",
#            "included_segments": ["Subscribed Users"],
#            "contents": {"en": "English Message"}}
#
# req = requests.post("https://onesignal.com/api/v1/notifications", headers=header, data=json.dumps(payload))
# print(req.status_code, req.reason)

# from onesignal import OneSignal, SegmentNotification
#
# client = OneSignal("f6cc14cd-b352-47a6-b352-23fcf3731f75", "Basic MjgwNzUwOTItOGIxYi00MDZmLThlZDMtNDI5ZTlhOGZhYzAw")
# notification_to_all_users = SegmentNotification(
#     contents={
#         "en": "test"
#     },
#     included_segments=SegmentNotification.ALL
# )
# client.send(notification_to_all_users)
from onesignal_sdk.client import Client

client = Client(app_id="f6cc14cd-b352-47a6-b352-23fcf3731f75",
                rest_api_key="ZjBkODdlMTktYzhjMC00NDYzLWEzMmItNjJkYWZkMTc3NWQ5",
                user_auth_key="MjgwNzUwOTItOGIxYi00MDZmLThlZDMtNDI5ZTlhOGZhYzAw")

notification_body = {
    'contents': {'en': "c'mon"},
    'included_segments': ['Subscribed Users']
}
response = client.send_notification(notification_body)
print(response.body)

# import requests
# import json

# header = {"Content-Type": "application/json; charset=utf-8",
#           "Authorization": "Basic MjgwNzUwOTItOGIxYi00MDZmLThlZDMtNDI5ZTlhOGZhYzAw"}
#
# payload = {"app_id": "f6cc14cd-b352-47a6-b352-23fcf3731f75",
#            "included_segments": ["Subscribed Users"],
#            "contents": {"en": "WELCOME"}}
#
# req = requests.post("https://onesignal.com/api/v1/notifications", headers=header, data=json.dumps(payload))
#
# print(req.status_code, req.reason)
