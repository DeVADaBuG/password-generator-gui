import tkinter as tk
import random
import string

def gen_pw():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

print(f"Generated Password: {gen_pw()}")
