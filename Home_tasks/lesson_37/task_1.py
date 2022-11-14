"""Download and save to file robots.txt from wikipedia, twitter websites etc."""

import requests

receive = requests.get('https://en.wikipedia.org/wiki/Robot_(disambiguation)')
with open (r'C:\Code\Beetroot\Home_tasks\lesson_37\Robots.txt', 'wb') as f:
    f.write(receive.content)
