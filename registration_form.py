import json
import time


def login_validation(login=''):
    with open('database.txt') as file:
        json_file = json.load(file)

    login_check = True
    error = ""

    if login.replace(' ', '') == '' or login.replace(' ', '') == "":
        login_check = False
        error += "login can not be empty\n"

    if login in json_file:
        login_check = False
        error += "This login is already exists\n"

    return login_check, error


def check_by_dict(password, symbols_dict):
    check = False
    for symbol in symbols_dict:
        if symbol in password:
            check = True

    return check


def password_validation(password=''):
    pass_check = True
    error = ""

    symbols = "!@#$%^&*()_+=-><?}{:[]|;,./"
    numbers = "1234567890"

    if password.replace(' ', '') == '' or password.replace(' ', '') == "":
        pass_check = False
        error += "password can not be empty.\n"

    if password.islower():
        pass_check = False
        error += "password mast have at least one capital letter.\n"

    if not check_by_dict(password, symbols):
        pass_check = False
        error += "password mast have at least one symbol letter.\n"

    if not check_by_dict(password, numbers):
        pass_check = False
        error += "password mast have at least one number letter.\n"

    if len(password) < 8:
        pass_check = False
        error += "password mast have at least 8 letters.\n"

    return pass_check, error


def create_new_account(login, password):
    with open('database.txt') as file:
        json_file = json.load(file)

    json_file[login] = {
        'password': password,
        'password_change_date': time.time(),
        'login_attempts': 0,
        'is_blocked': False
    }

    with open('database.txt', 'w') as file:
        json.dump(json_file, file)


def registration_form():
    while True:
        print("Registration form")
        ans_login = input("Login: ")
        ans_pass = input("Password: ")
        ans_pass_re = input("Re password: ")

        check_login, error_login = login_validation(ans_login)
        check_pass, error_pass = password_validation(ans_pass)

        if not check_login:
            print(error_login)
            continue

        elif ans_pass != ans_pass_re:
            print("Passwords are not similar")
            continue

        elif not check_pass:
            print(error_pass)
            continue

        else:
            create_new_account(ans_login, ans_pass)
            break
