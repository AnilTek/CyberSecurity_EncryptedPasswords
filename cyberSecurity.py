import numpy
import random
import time


alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
users = {}
password = input(f'please type your password so we can make it more secure :  ')
username = input(f'and please declare a username for this password : ')
ans = '1'

"""
Reminder!!!

This code is case sensetive please avoid create password that contains capital letters exp ---> A, B, C, etc..

"""





def createSecurePassword(password,username):
 
 """
 This is Method is used for 
 creating a more secure password from 
 given password

 it also stores the patern in users dict
 """
 u=0
 change_pattern = []
 password_chars = []
 for char in password:
    password_chars.append(char)

 password_chars.reverse()



 for patern_num in range(0,len(password_chars)):
    random_patern_number = random.randint(0,4)
    change_pattern.append(random_patern_number)
 print('-'*60)
 
 print(f"The pattern used in this password was : {change_pattern}")

 

 

   





 new_list = []

 for i in range(len(password_chars)):
    for j in range(len(alphabet)):
        if password_chars[i] == alphabet[j]:
            k = change_pattern[u]
            if j+k >= len(alphabet):
                new_index = (j+k) - len(alphabet)
                new_char = alphabet[new_index]
                new_list.append(new_char)
            else:
                new_char = alphabet[j+k]
                new_list.append(new_char)
            u += 1
                  
            
              

 secured_merged_password = ''.join(new_list)
 
 print(f"Encrypted Password : \033[1;32m{secured_merged_password}\033[0m")
 print('-'*60)

 users[username]= [new_list,change_pattern]


 


def contains_integer(string):
    """
    Checks if the password contains a integer value
    because the code doesnt work with numbers because of the alphabet list
    """
    for char in string:
        if char.isdigit():
            return True
    return False

#def resolveSecurePassword(securepassword,change_pattern)
def check_if_user_exists(users):
    """
    Checks if user already exists one password can be used twice but it 
    cant be declared on same username so this method checks the username
    given username must be unique
    """
    if username in users:
        return True
    else:
        return False
    
def resolve_the_password(username,users):

    """
    this method resolves the encrypted password 
    with the help of username dict method can access 
    the users dict and get the encrypted password and the 
    patern that used 
    """
    u=0
    print("\033[1;32mResolving...\033[0m")

    time.sleep(3)

    secured_password = users[username][0]
    secured_patern = users[username][1]

    resolved_list = []

    for i in range(len(secured_password)):
        for j in range(len(alphabet)):
           if secured_password[i] == alphabet[j]:
              k = secured_patern[u]
              new_char = alphabet[(j - k) % 26]  
              resolved_list.append(new_char)
              u += 1

    resolved_list.reverse() 
    resolved_password = ''.join(resolved_list)
    print('--'*30)
    print(f"Resolved Password : \033[1;32m{resolved_password}\033[0m")
    print('--'*30)



    
    





while contains_integer(password):

    password = input("Type your password so we can make it more secure: ")
    if contains_integer(password):
        print("String contains an integer. Please try again.")
    else:
        break

createSecurePassword(password=password, username=username)
print("\033[1;32mPassword Successfully Changed for better security\033[0m")



while ans == '1' or ans == '2':
    ans = input("Would you like to Create another secure password or resolve a secure password that already exists (1- CREATE / 2- RESOLVE): ")

    if ans == '1':
        password = input("Type your password so we can make it more secure: ")
        username = input("Please declare a username for this password: ")
        while contains_integer(password) or check_if_user_exists(users=users) :
            print("String contains an integer or the user is already exists. Please try again! ")
            password = input('Password :')
            username = input('Username :')
            
    
        createSecurePassword(password=password, username=username)
    elif ans == '2':
        check = input("Would you like to see the usernames in our database before the resolving process (y/n): ")
        if check == 'y':
            print(users)
        elif check == 'n':
            username_entry = input('Please type the username :')
            resolve_the_password(username=username_entry,users=users)

      
      
   








