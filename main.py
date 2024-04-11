def encode(password):
    new_password = ""
    password = str(password)
    for i in range(len(str(password))):
        new_password += str(int(password[i]) + 3)
    print(new_password)
    return int(new_password)

def main():
    password = 0
    #Print Menu
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
    try:
        choice = int(input("Please enter an option: "))
    except:
        print("Invalid Input! Please try again.")
    else:
        if choice == 1:
            #Ask user for proper input
            while True:
                try:
                    password = int(input("Please enter your password to encode: "))
                    password = encode(password)
                    print("Your password has been encoded and stored!\n")
                except:
                    print("Invalid Password Input! Please try again.")
                else:
                    break
        elif choice == 2:
            #Decode
            print(f"The encoded password is {password}, and the original password is {decode(password)}.\n")
            pass
        elif choice == 3:
            exit()
        else:
            print("Invalid Input!")

if __name__ == "__main__":
    while True:
        main()