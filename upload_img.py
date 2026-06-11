#!/usr/bin/env python3
import requests
import os

img_path = '/Users/wangjing/WorkBuddy/Claw/breakfast-menu.png'

# Try litterbox (temporary catbox)
try:
    with open(img_path, 'rb') as f:
        files = {'file': ('breakfast-menu.png', f, 'image/png')}
        r = requests.post('https://litterbox.catbox.moe/resources/internals/api.php', 
                          data={'reqtype': 'fileupload', 'time': '72h'}, 
                          files=files, timeout=60)
    print('Litterbox:', r.text)
except Exception as e:
    print(f'Litterbox failed: {e}')

# Try 0x0.st
try:
    with open(img_path, 'rb') as f:
        r = requests.post('https://0x0.st', 
                          files={'file': f}, timeout=60)
    print('0x0.st:', r.text)
except Exception as e:
    print(f'0x0.st failed: {e}')
