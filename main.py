#Timothy Bochkarev
def encode_pass(password):
    nstring = ""
    for char in password:
        num = int(char)
        if num < 7:
            num += 3
            nstring.append(num)
        else:
            if num == 7:
                nstring.append("0")
            elif num == 8:
                nstring.append('1')
            elif num == 9:
                nstring.append('2')
    global encoded
    encoded = nstring



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
            encode_pass(passw)
            print("Your password has been encoded and stored!")
            print()
        elif user_input == '2':
            pass