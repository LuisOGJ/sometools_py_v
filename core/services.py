import random
import string


def generatePassService(use_mayus, use_special, user_numbers, dist):
    notAdd = ":,\"/\\"
    c_minus = string.ascii_lowercase
    c_mayus = string.ascii_uppercase
    c_special = string.punctuation
    c_numbers = string.digits
    charactersPool = c_minus

    for c in notAdd:
        if c in c_special:
            c_special = c_special.replace(c, "")

    if use_mayus:
        charactersPool += c_mayus
    if use_special:
        charactersPool += c_special
    if user_numbers:
        charactersPool += c_numbers

    password = "".join(random.choice(charactersPool) for _ in range(dist))
    return password