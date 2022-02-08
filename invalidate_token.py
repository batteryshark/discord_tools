import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} token_to_expire")
        exit(-1)
    token_to_expire = sys.argv[1]
    r = requests.post("https://discord.com/api/v9/auth/logout",headers={'Authorization':token_to_expire},json={'token':token_to_expire})
    print(r.status_code)
    print(r.content)
    print("Done!")