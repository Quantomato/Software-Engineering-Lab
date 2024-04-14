def encode(password):
    new_password = ""
    for i in range(len(password)):
        new_password += str((int(password[i]) + 3)%10)
    return new_password

def decode(password):
    decoded = ''
    decoding = []
    for i in range(0, len(password)):
        decoding.append(decoded + str(int(password[i:i + 1]) - 3))
    for i in range(0,len(password)):
        if decoding[i] == '-3':
            decoded = decoded + str(7)
        elif decoding[i] == '-2':
            decoded = decoded + str(8)
        elif decoding[i] == '-1':
            decoded = decoded + str(9)
        else:
            decoded = decoded + str(decoding[i])
    return decoded

def main():
    global password
    # Print Menu
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
    try:
        choice = int(input("Please enter an option: "))
    except:
        print("Invalid Input! Please try again.")
    else:
        if choice == 1:
            # Ask user for proper input
            while True:
                try:
                    password_input = str(input("Please enter your password to encode: "))
                    password = encode(password_input)
                    print("Your password has been encoded and stored!\n")
                except:
                    print("Invalid Password Input! Please try again.")
                else:
                    break
        elif choice == 2:
            # Decode
            print(f"The encoded password is {password}, and the original password is {decode(password)}.\n")
            pass
        elif choice == 3:
            exit()
        else:
            print("Invalid Input!")


if __name__ == "__main__":
    while True:
        main()
