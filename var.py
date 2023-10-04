import os
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv(".env")

def make_int(str_input):
    str_list = str_input.split(" ")
    int_list = []
    for x in str_list:
        int_list.append(int(x))
    return int_list

class Var:
    API_ID = int(os.getenv("API_ID", "26439078"))
    API_HASH = os.getenv("API_HASH", "7fbe4d0da3109bee698d88b262d71630")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "6325577627:AAEHmQ0j0bK0JszJp_I_G9uCmONfWXUWaKE")
    sudo = os.getenv("SUDO", "6024212623 5218610039 6487519528")
    SUDO = []
    if sudo:
        SUDO = make_int(sudo)
