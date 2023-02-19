# Website Blocker script
# Block website access during predetermined hours

import time
from datetime import datetime as dt

hosts_path = "C:\Windows\System32\drivers\etc\hosts"

redirect = "127.0.0.1"

website_list = ["www.twitter.com", "twitter.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16):


