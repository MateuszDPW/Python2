import hashlib
#użycie SHA=256 do hashowania tekstu
text_to_hash = "Hello, World!"
hash_object = hashlib.sha256(text_to_hash.encode()) # Dane wejściowe muszą być typ...
hash_value = hash_object.hexdigest() # Zwraca wartość hash jako ciąg znaków szesnastkowych
print(hash_value)

#==============================#

# Dynamiczne wybieranie algorytmu hashującego
hash_type = "sha1"
dynamic_hash = hashlib.new(hash_type)
dynamic_hash.update(b"Hello, World!")
print(dynamic_hash.hexdigest())

#==============================#

# coś
class Product:
    name: ''
    quantity: 0

prod1 = Product()
prod2 = Product()

print(hash(prod1))
print(hash(prod2))

#==============================#

#hashowanie wiekszych danych
def hash_file(file_path):
    hash_obj = hashlib.sha256()
    with open(file_path, "rb") as file: #otworz plik w trybie binarnym
        for chunk in iter(lambda: file.read(4096), b""):    #czytaj plik blokami po...
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

# wywołanie funkcji na przykładowym pliku
file_hash = hash_file('example.txt')
print(file_hash)

#============================================#

import os

def secure_password_hash(password):
    salt = os.urandom(16) # Generuje bezpieczną sól
    key = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100000)
    return salt + key

# hashowanie hasła z bezpieczną solą
password = "bezpieczneHaslo123"
hashed_password = secure_password_hash(password)
print(hashed_password)

#============================================#
# Zadanie dla studentów
