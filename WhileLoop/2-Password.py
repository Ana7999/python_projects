username = input()
password = input() # prava lozinka



while True:
    data = input()  # lozinka za proveru
    if data == password:
        break
print(f"Welcome, {username}!")

