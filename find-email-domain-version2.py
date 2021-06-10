# Update the parseEmail() function to also separate out the extension segment
# of the domain.

# What additional tests, if any would you add to test this version of the function.

#====================
# Test input:
#     test
#     test@gmail
#     testgmail.com
#     test@@gmail.com
#     test@gmail..com
#     test@.com
#     test@gmail.
#     test@gmail.com
#====================

def parseEmail(emailAddress):

    def printInvalidWarning():
        print("----------------------------------------------------")
        print("Invalid email address format. Please try again.")
        print("----------------------------------------------------")

    if emailAddress.find("@") == -1 or \
       emailAddress.find(".") == -1 or \
       emailAddress.count("@") > 1:
        printInvalidWarning()
        return False

    # Separate before and after "@" symbol
    AtSymbolLocation = emailAddress.index("@")
    domainName = emailAddress[:AtSymbolLocation]
    domainAndExtension = emailAddress[AtSymbolLocation+1:]

    if domainAndExtension.count(".") > 1 or \
       domainAndExtension.startswith(".") or \
       domainAndExtension.endswith("."):
        printInvalidWarning()
        return False

    dotLocation = domainAndExtension.index(".")
    domain = domainAndExtension[:dotLocation]
    extension = domainAndExtension[dotLocation:]

    print("----------------------------------------------------")
    print("Domain Name: " + domainName)
    print("Domain: " + domain)
    print("Extension: " + extension)
    print("----------------------------------------------------")
    return True

emailAddressIsParsed = False

while not emailAddressIsParsed:
    emailAddress = str(input("Enter email address: "))
    emailAddressIsParsed = parseEmail(emailAddress)


