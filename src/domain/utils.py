import random
import string

def generate_code():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=6)) 
    return code