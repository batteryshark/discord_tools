# A POC for python-based Discord Gateway connection... no IPC required.
# Uses websocket_client
import websocket
import json
import time

token = "PASTE_TOKEN_OR_READ_IT_FROM_SOMEWHERE"
APP_ID = "PASTE_AN_APP_ID_HERE"

ws = websocket.WebSocket()
ws.connect("wss://gateway.discord.gg/?v=9&encoding=json")
heartbeat_interval = json.loads(ws.recv())['d']['heartbeat_interval']
res = ws.send(json.dumps({
    "op": 2,
    "d": {
        "token": token,
        "properties": {
            "$os": "windows",
            "$browser": "Discord",
            "$device": "desktop"
        }
    }
}))

print(res)

def clear_activity():
    activity = {
        "type": 0,
        "name": None,
        "state":None,
        "details": None,
    }
    payload = {
        "op": 3,
        "d": {
            "since": 999999999999999999999999999999999999999999999999999999999999999999999999999999999,
            "activities": [activity],
            "status": "online",
            "afk": False
        }
    }
    try:
        res = ws.send(json.dumps(payload))
        print(res)
    except:
        print("Error Clearing Activity Send")
        pass  
        
def send_activity(name,state, desc):
    activity = {
        "type": 0,
        "name": name,
        "state":state,
        "details": desc,
        "timestamps": {
				"start": int(time.time())
			},
        "application_id": REAL_APP_ID,
        "assets": {
				"large_image": "",
				"large_text": ""
        },
        "party": {
        },
        "secrets": {
            
        }
    }

    payload = {
        "op": 3,
        "d": {
            "since": 999999999999999999999999999999999999999999999999999999999999999999999999999999999,
            "activities": [activity],
            "status": "online",
            "afk": False
        }
    }

    try:
        res = ws.send(json.dumps(payload))
        print(res)
    except:
        print("Error Setting Activity Send")
        pass
        

    
send_activity("notepad.exe","Checking update","From Version 8675309")
time.sleep(20)		
clear_activity()
time.sleep(5)
ws.close()