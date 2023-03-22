#Timothy Bochkarev
def encode(password):
    nstring = ""
    for char in password:
        num = int(char)
        if num < 7:
            num += 3
            nstring += str(num)
        else:
            if num == 7:
                nstring += str("0")
            elif num == 8:
                nstring += str("1")
            elif num == 9:
                nstring += str("2")
    global encoded
    encoded = nstring
    return encoded

def decode(encoded_pass):
    encoded_pass = list(encoded_pass)
    count = 0
    for num in encoded_pass:
        new_num = int(num)
        encoded_pass[count] = new_num
        count += 1
    for i in range(len(encoded_pass)):
        if encoded_pass[i] > 2:
            encoded_pass[i] = encoded_pass[i] - 3
        else:
            if encoded_pass[i] == 2:
                encoded[i] = 9
            elif encoded_pass[i] == 1:
                encoded_pass[i] = 8
            else:
                encoded_pass[i] = 7
    nstring = ''
    for value in encoded_pass:
        nstring += str(value)
    return nstring


if __name__ == "__main__":
    encoded = ''
    user_input = 0
    while user_input != "3":
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        user_input = input("Please enter an option: ")
        if user_input == '1':
            passw = input("Please enter your password to encode: ")
            encoded_pass = encode(passw)
            print("Your password has been encoded and stored!")
            print()
        elif user_input == '2':
            print(f'The encoded password is {encoded_pass}, and the original password is {decode(encoded_pass)}.')