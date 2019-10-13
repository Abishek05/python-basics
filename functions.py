'''
def get_bank_balance():
    print("500")


get_bank_balance()
'''

dict = {
    'john': 500,
    'jane': 400,
    'jack': 600
}


def get_bank_balance(name):
    print(dict[name])

get_bank_balance('jack')
