def is_substring(main_str, sub_str):
    return sub_str in main_str

def count_occurrences(main_str,char):
    return main_str.count(char)

def replace_substring(main_str,old_sub, new_sub):
    return main_str.replace(old_sub,new_sub)

def to_capital_letters(main_str):
    return main_str.upper()

def menu():
    print("Menu:")
    print("to check")
    print("1.string is a substring of another string")
    print("2.Count occurance of character")
    print("3.Replace a substring with another substring")
    print("4.Convert to capital letters")
    print("5.exit")

def main():
    while True:
        menu()
        choice = input("Enter your choice (1-5):")

        if choice == '1':
            main_str=input("Enter your string:")
            sub_str =input("Enter the char:")
            if is_substring(main_str, sub_str):
                print(f"'{sub_str}' is a substring of '{main_str}'")
            else:
                print(f"'{sub_str}' is not a substring of '{main_str}'")
        elif choice == '2':
            main_str = input("enter the string:")
            char = input("Enter the character:")
            count = count_occurrences(main_str, char)
            print(f"The character '{char}' occurs '{count}' times in the given string")
        elif choice == '3':
            main_str = input("Enter the main string: ")
            old_sub = input("Enter the substring to be replaced: ")
            new_sub = input("Enter the new substring: ")
            new_str = replace_substring(main_str, old_sub, new_sub)
            print(f"The new string is: {new_str}")

        elif choice == '4':
            main_str = input("Enter the string: ")
            capital_str = to_capital_letters(main_str)
            print(f"The string in capital letters is: {capital_str}")

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
