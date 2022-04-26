

# This function generates the
# key in a cyclic manner until
# it's length isn't equal to
# the length of original text
def generateKey(string, keyIn):
    key = list(keyIn)
    if len(string) == len(key):
        return key
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return "".join(key)


# encrypted text generated
# with the help of the key
def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        #print(f"CHAR: {string[i]} Offset: {key[i]%26} CypherCHAR: {x}")
        rawX = (ord(string[i]) +
             ord(key[i])) % 26
        x = rawX + ord('A')
        #                   N       78      f       24      24      89      Y
        #       89 + 24 = 113 - 97
        #                   o       111     r       10      17      82      R

        # print(f"CHAR: {string[i]} ORD: {ord(string[i])} KEY: {key[i]} Offset: {ord(key[i]) % 26} CypherCHAR: {rawX} FINAL Value: {x} FinalCHAR: {chr(x)}")

        cipher_text.append(chr(x))

    return "".join(cipher_text)


def introduction():
     textoutput = '''
    This encryption System enables a user to enter free from txt or provide a file name
    where their text to encrypt may be found and will return an encrypterd version of that text
    for them to share with other users.


    '''
     return textoutput


def helpHelp(actionReq):
    userChoice = 1
    if actionReq.lower() == "login":
        print(" You must enter a valid userID/PW for an active account...\nRemember 'help' is not a valid UserId or Password \nPlease try again.")
        return
    if actionReq.lower() == "encrypt":
        print("Help for Encryption is as follows:...")
    elif actionReq == "decryption":
        print("Help for Decryption is as follows...")
    elif actionReq == 'overview':
       #print("This system........")
       print(f"{introduction()}")
    elif actionReq == 'intro':
        userChoice = welcomePage()
    return userChoice

def showEncryption(textIn):
    textOut = textIn
    return print(textOut)


def actionToTake(userReq, key, systemWord):
    sources = ['file', 'prompt']
    if userReq.lower() == 'help':
        print("...Help is on the way! ")
        # call help microservice
    elif userReq.lower() == "encrypt":
        source = input(f"What will be the source of your text to encrypt? {sources}")
        userText = None
        if source == 'file':
            fileIn = input(f"looking for a local file:...? ")
            with open(fileIn, "r") as inFile:
                userText = inFile.read()
        elif source == 'prompt':
            userText = input("We will start the Encryption as soon as you either hit enter... ")
        print("\n\t\t...Encrypting!")
        # Encrypt User Data from File or Input Prompt
        fileKey = generateKey(userText, systemWord)
        encrytpedText = cipherText(userText, fileKey)
        # Display Encrypted Results
        showEncryption(encrytpedText)

        # call encrypt microservice
    elif userReq.lower() == "decrypt":
        print("...Decrypting!")
        # call decrypt microservice
    elif userReq.lower() == "overview":
        helpHelp(userReq)
    elif userReq.lower() == "intro":
        helpHelp(userReq)
    else:
        print("Have a Nice Day!")
        # call goodbye microservice to close all services


def getUserReq(goodActions):
    req = input(f"How can we Help today? {goodActions} ")
    while req not in goodActions:
        req = input(f"Please use a keyword for us to better assist you today? {goodActions} ")
    return req


def addUser(userid, pw, key):
    with open("validUsers.txt", "a") as pwFile:
        print("Adding User to system ...")
        newUser = userid + pw
        cipher_text1 = cipherText(newUser, key)
        # print("Ciphertext :", cipher_text1)
        pwFile.write(f"{cipher_text1}   => {newUser}\n")
    pwFile.close()

    showUsers()



def login(key):
    userId = input("User ID: ")
    while userId == "help":
        helpHelp("login")
        userId = input("Enter a valid User ID: ")

    passWrd = input("Password: ")
    while passWrd == "help":
        helpHelp("login")
        passWrd = input("Enter a valid password: ")
    creds = cipherText(userId + passWrd, key)
    print(creds)
    with open("validUsers.txt", "r") as valids:
        data = valids.read()
        print("Data:", type(data),"\n",data)
        if creds not in data:
            print("it looks like you are a new user!\n Adding your credentials to our system.")
            addUser(userId, passWrd, key)
        else:
            print(f"{userId} has been Validated... Welcome.")

    return userId


def showUsers():
    print("# Displayed for testing purposes # \nEncypted Users...")
    with open("validUsers.txt", "r") as pwFileRead:
        print(pwFileRead.read())

def showMalUsers():
    print("# Displayed for testing purposes # \nEncypted Users...")
    with open("malUsers.txt", "r") as malFileRead:
        print(malFileRead.read())

def startServices(keyword):
    #####################################################
    # Build System Encryption Key to become a microService
    #keyword = "scuba"
    stringIn = 'myuseridandmyassociatedpasswordwithsomeextra'  # ??????????? ID + PW Length
    sysKey = generateKey(stringIn, keyword)
    #####################################################
    print("# Displayed for testing purposes #")
    with open("malUsers.txt", "w") as malFile:
        print("creating Malicious Users File...")
        malUser1 = "fred123"
        cipher_text1 = cipherText(malUser1, sysKey)
        #print("Ciphertext :", cipher_text1)
        malFile.write(f"{cipher_text1}\n")
    malFile.close()
    showMalUsers()


    with open("validUsers.txt", "w") as pwFile:
        print("creating PW File...")
        #addUser("dave", "123", key)
        mockUser1 = "dave123"
        cipher_text1 = cipherText(mockUser1, sysKey)
        #print("Ciphertext :", cipher_text1)
        pwFile.write(f"{cipher_text1}   => {mockUser1}\n")
        mockUser2 = "andrea456"
        cipher_text2 = cipherText(mockUser2, sysKey)
        #print("Ciphertext :", cipher_text2)
        pwFile.write(f"{cipher_text2} => {mockUser2}\n")
        mockUser3 = "fred123"
        cipher_text3 = cipherText(mockUser3, sysKey)
        # print("Ciphertext :", cipher_text2)
        pwFile.write(f"{cipher_text3}   => {mockUser3}\n")
    pwFile.close()
    showUsers()
    # print("Encypted Users...")
    # with open("validUsers.txt", "r") as pwFileRead:
    #     print(pwFileRead.read())
    return sysKey



def welcomePage():
    welcome = '''### AH Enterprises all rights reserved ###
    \n    Glad you have chosen to use this Encryption / Decryption 
    microservice, provided by AHE.\n
    It is an Encryption and Decryption service for users that are authorized to
    use the system. And it is based on the Vigenere Encryption Methodology.
    
    If at anytime you have a question on how to use this system, please type "help" 
    at any prompt and you will be directed to some guidance on how to proceed.
    '''
    menu = '''
        1. Login
        2. Help
        '''


    # call startup for all microservices and establish file structure

    print(f"{welcome}")

    print(f"{menu}")
    choice = int(input("Choice: "))
    while choice not in [1, 2]:
        choice = int(input("Please enter a valid Choice: "))

    return choice


def main():
    validActions = ['login', 'done', 'help', 'intro', 'overview', 'encrypt', 'decrypt']
    systemBaseText = "scuba"
    systemKey = startServices(systemBaseText)
    userchoice = welcomePage()
    user = None
    while userchoice == 2:
        userchoice = helpHelp("intro")

    if userchoice == 1:
        user = login(systemKey)
        done = False
        while not done:

            action = getUserReq(validActions)
            while action not in validActions:
                action = getUserReq(validActions)
                helpHelp("overview")
            if action.lower() != 'done':
                actionToTake(action, systemKey, systemBaseText)
            else:
                # sendEmail() # need to debug password problem
                print(f"Logging off {user}")
                print("Thanks for using the system")
                done = True



main()