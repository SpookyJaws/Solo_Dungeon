#defining repeated commands
from time import sleep
from os import system

#idk why i made this tbh
def t(Time = 0):
    sleep(Time)
def clr(Time = 1):
   system('clr')
   #unused for now since im working on tab ; - ;
   #print('\n' * 80)
   t(Time)
def sLoad():
    for i in range (2):
        for j in range(4):
            print('Loading', '. '*j)
            t(0.2)
            c()
            
#main output gen
def printer(text,x='',y=0, space = '', Time = 0.05):
    for i in range(len(text)):
        print(text[i], end = space)
        #changed it since it doesnt work as intended
    print('\n')
     
#huge ass function incoming    
def inputer(x='0'):
    x=x.lower()
    temp=(input()).lower()
    if x == 'yn':
        if temp in ('n','no','nah','nope','x','l'):
            return False
        elif temp in ('yes', 'yea', 'yeah', 'y', 'sure', 'uhuh', ' i think', 'i suppose', 'probably', 'most probably', 'w', 'why not', 'ye', 'yep', 'ya', 'yah', 'yeh', 'yuh', 'prolly'):
             return True
        if temp == 'why':
            printer('Because I said so faggot')
        else:
             printer("Undefined input.")
             printer('Write something that makes sense retard.')
             return inputer(x,y)
    if x == 'hub':
             if temp in ('quests', 'quest', '1', '1)', 'q'):
                 return '1'
             elif temp in ('player', 'p', '2', '2)', 'chr', 'character'):
                 return '2'
             elif temp in ('gates', 'gate', '3', '3)', 'g'):
                 return '3'
             elif temp in ('shop', 's', '4', '4)'):
                 return '4'
             elif temp in ('options', 'option', 'opt', 'o', '5', '5)'):
                 return '5'
             elif temp in ('help', 'h' '6', '6)'):
                 return '6'
             elif temp in ('save', 's', '7', '7)'):
                 return '7'
             elif temp in ('title', 'tit', 'tits', 't', '8', '8)'):
                 return '8'
             elif temp in ('easter egg', 'easteregg', 'cheat', 'cheats'):
                 return '9'
             else:
                 return False
    if x == 'gate':
        if temp in ('f','1','1)','f gate', 'fg', 'fgate', 'fgate '):
            return 'F'
        elif temp in ('d','1','1)','d gate', 'dg', 'dgate', 'dgate '):
            return 'D'
        elif temp in ('c','1','1)','c gate', 'cg', 'cgate', 'cgate '):
            return 'C'
        elif temp in ('b','1','1)','b gate', 'bg', 'bgate', 'bgate '):
            return 'B'
        elif temp in ('a','1','1)','a gate', 'ag', 'agate', 'agate '):
            return 'A'
        elif temp in ('s','1','1)','s gate', 'sg', 'sgate', 'sgate '):
            return 'S'
        else:
            return False
    if x == 'battle':
        if temp in ('1', '1)', 'attack', 'a', 'atk', ''):
            return 'a'
        elif temp in ('2', '2)', 'skill', 'skills', 's'):
            return 's'
        elif temp in ('3', '3)', 'player', 'plyr', 'p'):
            return 'p'
        elif temp in ('4', '4)', 'run', 'escape', 'x', 'n', 'e'):
            return 'e'
        else:
            return False