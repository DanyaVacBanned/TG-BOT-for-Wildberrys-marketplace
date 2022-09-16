import openpyxl
import random
def read_file():
    with open('text.txt', 'r', encoding='utf-8') as f:
        return str(f.read())

def get_token():
    book = openpyxl.open('BOT TOKEN.xlsx', read_only=True)
    sheet = book.active
    return str(sheet['A2'].value)


def pvz_text():
    with open('pvz_text.txt', 'r', encoding='utf-8') as f:
        return str(f.read())

def get_phone_number():
    book = openpyxl.open("BOT TOKEN.xlsx", read_only=True)
    sheet = book.active
    # i = str(random.randint(2,11))
    # val = 'C'+i
    return sheet['C2'].value



def feed_text_func():
    book = openpyxl.open('BOT TOKEN.xlsx', read_only=True)
    sheet = book.active
    i = str(random.randint(2,11))
    val = "E"+i
    return sheet[val].value


def get_price():
    book = openpyxl.open('BOT TOKEN.xlsx', read_only=True)
    sheet = book.active
    return sheet['A4'].value

def get_yooukassa():
    book = openpyxl.open('BOT TOKEN.xlsx', read_only=True)
    sheet = book.active
    return str(sheet['A3'].value)

def read_help_file():
    with open('help_file.txt', 'r', encoding='utf-8') as f:
        return str(f.read())