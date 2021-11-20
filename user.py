import sys
import requests
try:
    user = sys.argv[1]

    if len(sys.argv) <= 2:
        print(user)

    url = f'https://github.com/{user}'
    r = requests.get(url=url)
    if r.status_code == 200:
        print(f'Valid User: {user}')
    else:
        print(f'Invalid user: {user}')

except IndexError:
    print('No users specified')
