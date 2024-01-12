def say_hello(uname: str) -> str:
    return f'hello, {uname.lower()}'


if __name__ == '__main__':
    uinput = input('Enter your name: ')
    print(say_hello(uinput))
