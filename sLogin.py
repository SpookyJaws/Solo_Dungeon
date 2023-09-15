import pickle
from sFuncs import clr,t,printer,inputer
import sUserData
from sInterface import sMain

def Logger():
    clr()
    printer("Enter your name:",Time = 0.1)
    name = input()
    print('\n')
    file = open('userdata.dat', 'rb')
    try:
        while True:
            sUserData.sData = pickle.load(file)
            if sUserData.sData['Name'].lower() == name.lower():
                 printer(f"Welcome back {sUserData.sData['Name']}")
                 t()
                 sMain('hub_main.txt','hub')
    except EOFError:
        file.close()
        t()
        printer("User not found")
        t()
        printer("Are you a new user?")
        choice = inputer('YN')
        if choice == True:
            printer(f"Create new user {name}?")
            choice = inputer('YN')
            if choice == True:
                with open('userdata.dat', 'ab') as file:
# { 'Name' : name, 'Level' : 1, 'Exp' : 1, 'Stats' : 0, 'Crystals' : 0, 'Vit' : 10, 'Str' : 10, 'Wis' : 10, 'Dex' : 10, 'Sen' : 10, 'Items' : [], 'Skills' : [] }
                    pickle.dump({ 'Name' : name, 'Level' : 1, 'Exp' : 1, 'Stats' : 0, 'Crystals' : 0, 'Vit' : 10, 'Str' : 10, 'Wis' : 10, 'Dex' : 10, 'Sen' : 10, 'Items' : [], 'Skills' : [] }, file)
    Logger()    
    
#for dev purpouses
Logger()