#Main Interface
import sUserData as ud
from sFuncs import clr, t, printer, inputer
global sData
from random import randint
import sBattle

def checker(no,c = 0,end = 0):
    if no in ('heal_check\n'):
        if no == 'heal_check\n':
            if ud.sData['Vit'] * 10 != ud.sHealth:
                printer("You take a rest in a nearby inn to recover")
                t(0.5)
                x,y =  ud.heal()
                print(f'HP: {x} ----> {ud.sHealth}\
                MP: {y} ----> {ud.sMana}')
                t(0.5)               
    elif no in '1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n':
        if no == '1\n':
            print('\n' * 1)
        if no == '2\n':
            print('\n' * 2)
        if no == '3\n':
            print('\n' * 3)
        if no == '4\n':
            print('\n' * 4)
        if no == '5\n':
            print('\n' * 5)
        if no == '6\n':
            print('\n' * 6)
        if no == '7\n':
            print('\n' * 7)
        if no == '8\n':
            print('\n' * 8)
        if no == '9\n':
            print('\n' * 9)
        if no == '10\n':
            print('\n' * 10)
    elif no[:3].upper() == 'POG':
        temp = ''
        for i in range(3, len(no)):
            temp = temp + no[i]
        t(0.5)
        print(temp)
    else:
        printer(no)        

#main interface for most game interactions
def sMain(file,choice,file_length = 15, type = 'hub'):
    fReader = open(file)
    fLines = fReader.readlines()
    try:
        i = 0
        clr()
        while True:
            ud.PD()
            c = 0
            while True:
                checker(fLines[0])
                del fLines[0]
                c += 1
                if c == file_length:
                    break
            print('= ' * 48 + '\n')
            print('Press Enter to continue:    ')
            input()
    except IndexError:
        print('= ' * 50)
    printer('Choice: ')
    temp = choice
    ch = inputer(choice)
    selector(ch,file,temp,file_length,type)
    
def selector(ch,file,temp,file_length,type):
    if type == 'hub':
        if ch == '3':
            sMain('gate_select.txt','gate',13,'gate')
    if type == 'gate':
            temp = randint(1,3)
            sBattle.gate(ch + str(temp))
    else:
        printer("Invalid Input. Try Again")
    sMain(file,temp,file_length,type)