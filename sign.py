print('Select By Number:\n1) Login\n2) Sign Up')
x = int(input("=>"))
file = open('data.txt', 'r')
lst = file.readlines()
file.close()
if x == 1:
    validity = 0
    for i in range(5):
        if validity == 0:
            user = str(input("Username: "))
            pas = str(input("Password: "))
            for line in lst:
                cred = line.split(' ')
                if (str(cred[0]) == user) and (str(cred[1].strip()) == pas):
                    validity = 1
                    print('Login Successful!')
            if validity == 0:
                print('Incorrect Credentials')
    if validity == 0:
        print('You have no more login attempts left')
        v = input("Press enter to exit the program...")
        quit()

elif x == 2:
    validity = 0
    for i in range(999):
        done = 0
        if validity == 0:
            user = str(input("Enter Username: "))
            pas = str(input("Enter Password: "))
            for line in lst:
                cred = line.split(' ')
                if user == cred[0]:
                    print('Username already exists...')
                    done = 1
            if done == 0:
                file = open('data.txt', 'w')
                lst.append(user + ' ' + pas + '\n')
                inp = file.writelines(lst)
                file.close()
                validity = 1
                print('Successfully Signed Up!')
        else:
            v = input("Press enter to exit the program...")
            quit()




