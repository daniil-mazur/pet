import requests
import image
import os
import sys


get1 = requests.get('http://google.com')
print(get1)

get2 = requests.get('https://sun9-38.userapi.com/impg/JWCgjISACY_BvPhxZ3Ni_XdWzF7EgGB6sSSyHg/pS05wN0t_20.jpg?size=1440x2160&quality=95&sign=e84cc5f305d5613fdb47e0e55d604944&type=album')
with open('new_image.png', 'wb') as f:
    f.write(get2.content)
