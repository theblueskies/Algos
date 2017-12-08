import os
import requests
import time
import datetime


def announce():
    os.system('say "Hey Dana, bestsock is live"')


def get_page():
    url = 'https://bestself.co/pages/black-friday-landing-page-monday'
    while True:
        response = requests.get(url)
        if response.status_code == 200:
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            while True:
                announce()
        else:
            print('Sleeping a little...')
            time.sleep(120)


if __name__ == '__main__':
    get_page()
