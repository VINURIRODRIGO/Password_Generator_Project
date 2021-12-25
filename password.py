# Password Generator Project
import random

LETTER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
          'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
          'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
          'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@', '^', '_', '-']


class Password:
    def __init__(self):
        self.nr_letters = random.randint(8, 10)
        self.nr_symbols = random.randint(2, 4)
        self.nr_numbers = random.randint(2, 4)
        self.password_list = [random.choice(LETTER) for _ in range(self.nr_letters)]
        self.create_password()

    def create_password(self):
        self.password_list += [random.choice(SYMBOLS) for _ in range(self.nr_symbols)]
        self.password_list += [random.choice(NUMBERS) for _ in range(self.nr_numbers)]
        random.shuffle(self.password_list)

    def password(self):
        password = ""
        for char in self.password_list:
            password += char
        return password


# Check the strength of the password
def password_checker(password):
    x = []
    if len(password) > 8:
        for _ in password:
            if LETTER.count(_) != 0:
                x.append("letter")
            elif SYMBOLS.count(_) != 0:
                x.append("symbol")
            elif NUMBERS.count(_) != 0:
                x.append("number")
    if x.count("letter") != 0 and x.count("symbol") != 0 and x.count("number") != 0:
        return True
    return False
