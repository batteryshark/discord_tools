import requests


token = "PASTE_TOKEN_HERE"
CLIENT_ID = "PASTE_CLIENT_ID_HERE"

headers = {
'authorization':token
}
data = {
    "events": [
        {
            "properties": {
                "accessibility_features": 256,
                "accessibility_support_enabled": False,
                "app_id": CLIENT_ID,
                "client_performance_cpu": 0,
                "client_performance_memory": 325508,
                "client_send_timestamp": 1643067405710,
                "client_track_timestamp": 1643067405699,
                "client_uuid": "",
                "rendered_locale": "en-US",
                "transport": "ipc"
            },
            "type": "authorized_app_connected"
        }
    ],
    "token": ""
}
#r = requests.post("https://discord.com/api/v9/science",headers=headers,json=data,verify=False)

#r = requests.get("https://discord.com/api/v9/users/@me/billing/payment-sources",headers=headers)
r = requests.get(f"https://discord.com/api/v9/oauth2/applications/{CLIENT_ID}/assets",headers=headers)
print(r.status_code)
print(r.content)
r = requests.get(f"https://discord.com/api/v9/oauth2/applications/{CLIENT_ID}/rpc",headers=headers)
print(r.status_code)
print(r.content)