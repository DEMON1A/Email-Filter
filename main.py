import sys , random , string , os
from colorama import Fore

# Get User Input And Check It
def GetInputs():
    EmailList = str(input(Fore.BLUE + "List: "))
    if EmailList == '':
        print(Fore.RED + "Error: EmailList Required.")
        EmailList = str(input(Fore.BLUE + "List: "))
        if EmailList == '':
            print(Fore.BLUE + "OK.")
            sys.exit()
        else:
            pass
    else:
        pass

    try:
        EmailList = open(EmailList , 'r')
        return EmailList
    except Exception:
        print(Fore.RED + "Error: Can't Open {0}".format(EmailList))
        sys.exit()

# Start Lists Counters
def GmailCounter(GmailList):
    Count = 0
    for i in GmailList:
        Count +=1

    return Count

def YahooCounter(YahooList):
    Count = 0
    for i in YahooList:
        Count += 1

    return Count

def HotmailCounter(HotmailList):
    Count = 0
    for i in HotmailList:
        Count += 1

    return Count

def OutlookCounter(OutlookList):
    Count = 0
    for i in OutlookList:
        Count += 1

    return Count

def WrongDataCounter(WrongList):
    Count = 0
    for i in WrongList:
        Count += 1

    return Count
# End Lists Counters

# Start Genrate Random Strings For File Names
# From ( https://pynative.com/python-generate-random-string/ )
def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
# End Genrate Random Strings For File Names

def Main():
    # Start Defines Filter Bases
    Gmail = "@gmail.com"
    Yahoo = "@yahoo.com"
    Hotmail = "@hotmail.com"
    Outlook = "@outlook.com"
    # You Could Define New Emails Here And Manage The Code To Filter It Too Here
    # Or You Could Contact Me At: mdaif1332@gmail.com
    # End Defines Filter Bases

    # Start Build Lists For Save Data
    GmailList = []
    YahooList = []
    HotmailList = []
    OutlookList = []
    WrongData = []
    # End Build Lists For Save Data

    # Start Get EmailList From User Input
    FileList = GetInputs()
    # End Get EmailList From User Input

    # Start Filter Data And Save It To Lists
    print("\n")
    for Email in FileList:
        Email = Email.rstrip('\n')
        if Gmail in Email:
            GmailList.append(Email)
            print(Fore.GREEN + "[INFO]" + Fore.BLUE + " Got " + Fore.RED + "Gmail" + Fore.BLUE + " Email." + Fore.GREEN + " [INFO]")
        elif Yahoo in Email:
            YahooList.append(Email)
            print(Fore.GREEN + "[INFO]" + Fore.BLUE + " Got " + Fore.RED + "Yahoo" + Fore.BLUE + " Email." + Fore.GREEN + " [INFO]")
        elif Hotmail in Email:
            HotmailList.append(Email)
            print(Fore.GREEN + "[INFO]" + Fore.BLUE + " Got " + Fore.RED + "Hotmail" + Fore.BLUE + " Email." + Fore.GREEN + " [INFO]")
        elif Outlook in Email:
            OutlookList.append(Email)
            print(Fore.GREEN + "[INFO]" + Fore.BLUE + " Got " + Fore.RED + "Outlook" + Fore.BLUE + " Email." + Fore.GREEN + " [INFO]")
        else:
            WrongData.append(Email)
            print(Fore.RED + "[FAIL]" + Fore.YELLOW + " Got Wrong Email." + Fore.RED + " [FAIL]")
    # End Filter Data And Save It To Lists

    # Start Count Lists
    GmailCount = GmailCounter(GmailList=GmailList)
    YahooCount = YahooCounter(YahooList=YahooList)
    HotmailCount = HotmailCounter(HotmailList=HotmailList)
    OutlookCount = OutlookCounter(OutlookList=OutlookList)
    WrongDataCount = WrongDataCounter(WrongList=WrongData)
    # End Count Lists

    # Start Print Results
    print(Fore.GREEN + "\nResults:")
    print(Fore.YELLOW + "Number Of GmailEmails = {0}".format(GmailCount))
    print(Fore.YELLOW + "Number Of YahooEmails = {0}".format(YahooCount))
    print(Fore.YELLOW + "Number Of HotmailEmails = {0}".format(HotmailCount))
    print(Fore.YELLOW + "Number Of OutlookEmails = {0}".format(OutlookCount))
    print(Fore.YELLOW + "Number Of WrongEmails = {0}".format(WrongDataCount))
    # End Print Results

    SaveQuestion = str(input(Fore.BLUE + "\nWanna Save Data? (Y . N): "))
    
    # Start Creating Program Data Folder If Not Exists
    try:
        os.mkdir('ProgramData')
        print(Fore.YELLOW + "ProgramData Folder Created")
    except Exception:
        print(Fore.YELLOW + "ProgramData Folder Exists, No Need To Create It.")
    # End Creating Program Data Folder If Not Exists

    if SaveQuestion.lower() == "y":
        randomFileToken = randomString()
        with open('ProgramData/gmail-emails-{0}'.format(randomFileToken) , 'a') as gmailFile:
            for Gmail in GmailList:
                gmailFile.write(Gmail + "\n")

        with open('ProgramData/yahoo-email-{0}'.format(randomFileToken) , 'a') as yahooFile:
            for Yahoo in YahooList:
                yahooFile.write(Yahoo + "\n")

        with open('ProgramData/hotmail-email-{0}'.format(randomFileToken) , 'a') as hotmailFile:
            for Hotmail in HotmailList:
                hotmailFile.write(Hotmail + "\n")

        with open('ProgramData/outlook-list-{0}'.format(randomFileToken) , 'a') as outlookFile:
            for Outlook in OutlookList:
                outlookFile.write(Outlook + "\n")

        with open('ProgramData/wrong-emails-{0}'.format(randomFileToken) , 'a') as wrongFile:
            for Email in WrongData:
                wrongFile.write(Email + "\n")

        print(Fore.YELLOW + "Done, Check Your ProgramData Folder For Filtred Data.")
        print(Fore.YELLOW + "Your File Token Is {0}".format(randomFileToken))
        print(Fore.YELLOW + "To Remove All Of Program File: Type -> rm *-{0}".format(randomFileToken))
        print(Fore.BLUE + "\nAll Data Saved.")
    else:
        print(Fore.BLUE + 'OK.')
        sys.exit()

if __name__ == "__main__":
    Main()