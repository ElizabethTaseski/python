import os


def encrypt(text):
    """Encrypt text using ROT3."""
    charSet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\}]{[\"':;?/>.<, "
    encText = "".join([charSet[(charSet.find(c)+3)%95] for c in text])
    print(encText)
     

def decrypt(text):
    """Decrypt text using ROT3."""
    charSet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\}]{[\"':;?/>.<, "
    encText = "".join([charSet[(charSet.find(c)-3)%95] for c in text])
    print(encText)
 


FILE_PATH = 'file.txt'


def add_credentials():
    """Add new credentials to the file."""
    username = input("Enter username: ")
    password = input("Enter password: ")
    encrypted_password = encrypt(password)
    url = input("Enter URL: ")
    
    

    f=open(FILE_PATH, 'a')
    f.write(f"{username} | {encrypted_password} | {url}\n")
    print("Credentials added successfully!")

def view_credentials():
    """View stored credentials from the file."""
    if not os.path.isfile(FILE_PATH):
        print("No credentials file found.")
        return
    
    f = open("file.txt", "r")
    data = f.read() # 'data' now contains the contents of the file as a string
    print(data)
    if data != "":
        print("yes there's credentials")    
    else:
        print("no credentials found")
    
    
        
def main():
    
    
    choice = ''
    while choice != '3':
        print("\nPassword Manager")
        print("[1] Add credentials")
        print("[2] View credentials")
        print("[3] Exit")

        choice = input("\nMake your choice: ")
        
        if choice == '1':
            add_credentials()
        elif choice == '2':
            view_credentials()
        elif choice == '3':
            print("Exiting the program...")
        else:
            print("Invalid option, please try again.")
    
    print("Program exit.")

if __name__ == "__main__":
    main()
