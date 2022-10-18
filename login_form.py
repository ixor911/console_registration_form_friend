import json
import time


def user_check(login):
    with open('database.txt') as file:
        json_file = json.load(file)

    check = True
    error = ""

    if login not in json_file:
        check = False
        error += "there is no such user\n"
    elif json_file[login].get('is_blocked'):
        check = False
        error += "this user was blocked\n"

    return check, error


def pass_check(login, password):
    with open('database.txt') as file:
        json_file = json.load(file)

    check = False

    if password == json_file[login].get('password'):
        json_file[login]['login_attempts'] = 0
        check = True
    else:
        json_file[login]['login_attempts'] += 1

        if json_file[login].get('login_attempts') == 3:
            json_file[login]['is_blocked'] = True

    with open('database.txt', 'w') as file:
        json.dump(json_file, file)

    return check


def get_user(login):
    with open('database.txt') as file:
        json_file = json.load(file)

    return json_file[login]


def check_pass_time(user):
    check = True

    if int(user['password_change_date']) + 2628002 < time.time():
        check = False

    return check


def login_form():
    while True:
        print('Login form')
        ans_login = input("Login: ")
        ans_pass = input("Password: ")

        check_login, error_login = user_check(ans_login)

        if check_login:
            if pass_check(ans_login, ans_pass):
                print(f"You have entered as {ans_login}")

                user_data = get_user(ans_login)

                if not check_pass_time(user_data):
                    print("your password is old, we recommend you to change it")

                break

            else:
                print("wrong password")
        else:
            print(error_login)
            break

