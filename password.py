#тут будет генерироваться пароль при помощи определенной библиотеки
import secrets

def create_new(length, characters):
    return "".join(secrets.choice(characters) for i in range(length))