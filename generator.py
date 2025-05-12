import random
import string

LENGTH = 12
alphabet = string.ascii_letters + string.digits + string.punctuation

def generate_password():
    password = ''.join(random.choice(alphabet) for i in range(LENGTH))
    return password
        
password = generate_password()
print(password)
    
