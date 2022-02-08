import requests
import json
import logging

# These two lines enable debugging at httplib level (requests->urllib3->http.client)
# You will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
# The only thing missing will be the response.body which is not logged.
try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client
http_client.HTTPConnection.debuglevel = 1

# You must initialize logging, otherwise you'll not see debug output.
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

def get_token():
    uname = input("Enter Discord Username: ")
    upass = input("Enter Discord Password: ")
    data = {"login":uname,"password":upass,"undelete":False,"captcha_key":None,"login_source":None,"gift_code_sku_id":None}
    r = requests.post("https://discord.com/api/v9/auth/login",json=data)
    if r.status_code != 200:
        print("Error on Login")
        return False,""
    resp = r.json()
    # If we don't have MFA, just return the token
    if(resp['token']):
        return True,resp['token']
    # Otherwise, we have to hit totp
    code = input("Enter 2FA Code: ")
    data = {"code":code,"ticket":resp['ticket'],"login_source":None,"gift_code_sku_id":None}
    r = requests.post("https://discord.com/api/v9/auth/mfa/totp",json=data)
    if r.status_code != 200:
        print("Error on TOTP")
        return False,""   
    return True,r.json()['token']
    
    
res,token = get_token()
if not res:
    print("Error Getting Token")
else:
    print(f"Token: {token}")
    print("DO NOT GIVE THIS TO ANYONE")
