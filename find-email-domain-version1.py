# Write a function: parseEmail(emailAddress) which takes a single parameter, 'emailAddress'.
# The parameter should be an email address in the form: username@domain.ext
# Separate the address into two components and print each of these separately
#    1. The username
#    2. The domain and extension
   
# (Hint: See if you can find the index of the 'at' symbol)

# What test inputs can you give to your function to make sure it is 
# working as expected?


#====================
# Test input:
#     test@gmail
#     test@gmail@gmail.com
#     test@gmail.com
#====================


def parseEmail(emailAddress):
    if emailAddress.find("@") == -1 or \
       emailAddress.find(".") == -1 or \
       emailAddress.count("@") > 1:
        print("----------------------------------------------------")
        print("The text is not the email address format. Try again.")
        print("----------------------------------------------------")
        return False

    AtSymbolLocation = emailAddress.index("@")
    domainName = emailAddress[:AtSymbolLocation]
    domainAndExtension = emailAddress[AtSymbolLocation+1:]
    print("----------------------------------------------------")
    print("Domain Name is: " + domainName)
    print("Domain + Extension is: " + domainAndExtension)
    print("----------------------------------------------------")
    return True

emailAddressIsParsed = False

while not emailAddressIsParsed:
    emailAddress = str(input("Enter email address: "))
    emailAddressIsParsed = parseEmail(emailAddress)