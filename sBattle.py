import sFuncs as sf
import sMinigames as sm
import sInterface as si
from random import randint
from sUserData import PD, sData, sHealth, sMana
import sSkills

cp = '█'
ep = '░'
def gate(rank, length = 10, walc = 0):
    sf.clr()
    PD()
    sf.t()
    string = ''
    if walc > 0:
        for i in range(walc):
            string = string + cp
    for i in range(walc,length):
        string = string + ep
    print("=============================== DUNGEON  PROGRESS ===============================")
    sf.t()
    print("\t\t\t\t╔" + "═" * length + "╗")
    print("\t\t\t\t║" + string + "║")
    print("\t\t\t\t╚" + "═" * length + "╝") 
    sf.t(1)
    print()
    if walc == length:
        sf.t(1)
        sf.printer('You have completed the gate')
        sf.t(1)
        sf.printer('Returning back to hub...')
        sf.t(1)
        si.sMain('hub_main.txt','hub')
    else:
        if walc % 5 == 0 and walc != 0:
            sm.mG(rank[0])
            if walc % 10 == 0:
                sf.t()
                sf.printer('You have reached the final door')
                t(1.5)
                sf.printer('After a quick breath, you face the Dungeon Boss')
                sf.t()
                battle_sequence(rank, 'boss')   
        else:
            temp = randint(1,2)
            if temp == 2:
                sf.printer('!!!')
                sf.t()
                Data = enemies(rank, 'mob')
                if sUserData.sData['Lvl'] <= Data['Level_min']:
                    LVL = Data['Level_min']
                elif sUserData.sData['Lvl'] < Data['Level_max']:
                    LVL = sUserData.sData['Lvl']
                else:
                    LVL = Data['Level_max'] 
                battle_sequence(Data, LVL, rank)
            else:
                bg_text()
    gate(x,length,walc + 1)
            
def bg_text():            
#
# {'Name' : x, 'Level_min' : x, 'Level_max' : x, 'Sprite' : '', 'Stats' : ''}
#Attacker
#, 'Stats' : (15,25,25,20,15)
#Defender
#, 'Stats' : (30,20,20,15,15)
#Support
#, 'Stats' : (20,20,20,20,20)
#

def enemy_stater(level, stats):
    object = [0,0,0,0,0]
    a_stats = 0
    stat_check_temp = 0
    for i in range(level):
        if 1//10 < 5:
            a_stats += (5 * (i // 10 + 1))
        if i // 10 >= 5:
            a_stats += (10 * (i // 10 + 1))
        if i // 10 >= 10:
            a_stats += (100 * (i // 10 + 1))
    for i in range(a_stats):
        temp = randint(1,100)
        if temp <= stats[0]:
            object[0] += 1
        elif temp <= stats[0] +stats[1]:
            object[1] += 1
        elif temp <= stats[0] + stats[1] + stats[2]:
            object[2] += 1
        elif temp <= stats[0] + stats[1] + stats[2] + stats[3]:
            object[3] += 1
        else:
            object[4] += 1
    return object
                
def battle_sequence(Data, LVL, rank, flag = True):
    clear, run = False, False
    while True:
        if clear == True:
            break
        PD()
        sf.clr()
        if flag == True:
            sf.printer(f"You have encountered \" {Data['Name']} \" ")
            flag = False
            print(Data['Sprite'])
            object = enemy_stater(LVL, Data['Stats'])
            eHealth = object[0] * 10
        print(f"Enemy Health: {eHealth}")
        print('\n'*8)
        print("1) Attack \t\t 2) Skill \t\t 3) Player \t\t 4) Escape")
        temp = 0
        while True:
            temp = sf.inputer('battle')
            if temp == False:
                sf.printer("Invalid Input")
                t()
                sf.printer("Please try again:")
            else:
                break
        if temp == 'a':
            Attack()
        elif temp == 's':
            Skill()
        elif temp == 'p':
            Player()
        elif temp == 'e':
            x = randint(1,100)
        if x >= 80:
            sf.printer("You successfully manage to run away like a fucking pussy")
            clear = True
            run = True
        else:
            sf.printer("You refuse the thought to run away because you aren't a fucking pussy")
            eAttack()
        if eHealth <= 0:
            sf.printer('You have successfully defeated " {Data["Name"]} " ')
            print()
            sf.t()
            clear = True
        else:
            eAI(Data, object)
    if run != True:
        mG_win(rank, 0.1)

def eAI(Data, object):
    choice = randint(1,3)
    flag = True
    if choice in (1, 2):
        thing = sSkills.skills(Data['Skills'])
        