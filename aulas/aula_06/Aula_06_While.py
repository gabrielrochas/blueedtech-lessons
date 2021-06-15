# Piece of code to verify password
# This program will ask the user to enter a password and only exit when the password it is correct
password = '1234abcd';

checkPass = '';

while checkPass != password:
    checkPass = str(input("Digite a senha: "));
    if checkPass != password:
        print("Wrong password. Try again\n")
    else:
        print("Welcome back, gafanhoto!")