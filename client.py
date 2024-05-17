import requests

HOST = 'http://127.0.0.1:8888'


def get_main():
    endpoint = f'{HOST}'
    r = requests.get(url=endpoint)
    if r.status_code == 200:
        print(r.text)
    else:
        raise ValueError('Check ur server')


def get_hello():
    endpoint = f'{HOST}/api/hello'
    r = requests.get(url=endpoint)
    if r.status_code == 200:
        print(r.json())
    else:
        raise ValueError('Check ur server')


def get_random_name():
    endpoint = f'{HOST}/api/random'
    r = requests.get(url=endpoint)
    if r.status_code == 200:
        print(r.text)
    else:
        raise ValueError('Check ur server')


if __name__ == '__main__':
    get_main()
    get_hello()
    input('Click to continue')
    get_random_name()

