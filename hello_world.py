def say_hello():
    print("Hello World!")


def open_file():
    file = open("hello_world.py", "r")
    print(file.read())
    file.close()


def open_url():
    import urllib.request
    url = "https://www.google.com"
    response = urllib.request.urlopen(url)
    print(response.read())


if __name__ == '__main__':
    print('Hello World!')
    say_hello()
