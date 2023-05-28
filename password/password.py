from re import compile
from secrets import choice
from string import ascii_letters, digits, ascii_uppercase

p = compile('[01OIl]')


def random_password(length=8):
    candidates = p.sub('', ascii_letters + digits)
    uppercase = p.sub('', ascii_uppercase)
    numbers = p.sub('', digits)
    password = (''.join([choice(candidates) for _ in range(3)])
                + choice(uppercase)
                + choice(numbers)
                + ''.join([choice(candidates) for _ in range(length - 5)]))
    return password


if __name__ == '__main__':
    print(random_password(8))
