import json
import time
from registration_form import registration_form
from login_form import login_form


def menu_form():
    while True:
        ans = input("\n1. Registration\n"
                    "2. Login\n"
                    "0. Exit\n")
        ans = ans.replace(' ', '')

        if ans == '1':
            registration_form()
        elif ans == '2':
            login_form()
        elif ans == '0':
            break
        else:
            print("There is no such command!!")




