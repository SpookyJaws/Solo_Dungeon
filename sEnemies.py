from random import randint


#
# {'Name' : x, 'Level_min' : x, 'Level_max' : x}
#Attacker
#, 'Stats' : (15,25,25,20,15)
#Defender
#, 'Stats' : (30,20,20,15,15)
#Support
#, 'Stats' : (20,20,20,20,20)
#
#, 'Skills' : []


def enemies(type, Class = mob):
    type = type.lower()
    temp = randint(1,3)
    # 'Sprite' : None
    if type == 'f1':
        if Class == 'mob':
            if temp == 1:
                #Ice Porcupine
                return {'Name' : 'Ice Porcupine', 'Level_min' : 1, 'Level_max' : 2,  'Sprite' : None, 'Stats' : (30,20,20,15,15), 'Skills' : []}
            if temp == 2:
                #Rat Man
                return {'Name' : 'Rat Man', 'Level_min' : 2, 'Level_max' : 5,  'Sprite' : None, 'Stats' : (15,25,25,20,15), 'Skills' : []}
            if temp == 3:
                #Ratatat
                return {'Name' : 'Ratatat', 'Level_min' : 1, 'Level_max' : 3,  'Sprite' : None, 'Stats' : (20,20,20,20,20), 'Skills' : []}
        else:
            return  {'Name' : 'TheFatRat', 'Level_min' : 5, 'Level_max' : 10, 'Stats' : (30,20,20,15,15), 'Skills' : ['Slam']}
    if type == 'f2':
        if Class == mob:
            pic = '''
            /\
          _\\|\
          \_\|/__________
             /            _        _\
            | ___      I_I    _|_|____
            |  \__               _______|
              \___    ___ • _/
                   /       \
                  / /       |
                / /      ,   |\
               |_\   ___ /_\
                  /_____\
                   _||   ||_             
            '''
            if temp == 1:
                #Joe-blin
                return {'Name' : 'Weak Goblin', 'Level_min' : 1, 'Level_max' : 2, 'Sprite' : pic, , 'Stats' : (20,20,20,20,20), 'Skills' : []}
            if temp == 2:
                #Baby Goblin
                return {'Name' : 'Baby Goblin', 'Level_min' : 2, 'Level_max' : 5, 'Sprite' = pic, 'Stats' : (15,25,25,20,15), 'Skills' : []}
            if temp == 3:
                #gob
                return {'Name' : 'gob', 'Level_min' : 1, 'Level_max' : 3, 'Sprite' = pic, 'Stats' : (30,20,20,15,15), 'Skills' : []}
        else:
            return {'Name' : 'Joe - blin', 'Level_min' : 5, 'Level_max' : 10, 'Sprite' : None, 'Stats' : (15,25,25,20,15), 'Skills' : ['Gooblin']}
    if type == 'f3':
        if Class == mob:           
            if temp == 1:
                #Slime
                return {'Name' : 'Slime', 'Level_min' : 1, 'Level_max' : 2,  'Sprite' : None, 'Stats' : (20,20,20,20,20), 'Skills' : []}
            if temp == 2:
                #Non-Viscous slime (?)
                return {'Name' : 'Non-Wet Slime', 'Level_min' : 2, 'Level_max' : 5,  'Sprite' : None, 'Stats' : (30,20,20,15,15), 'Skills' : []}
            if temp == 3:
                #Ooze
                return {'Name' : 'Ooze', 'Level_min' : 1, 'Level_max' : 3,  'Sprite' : None, 'Stats' : (15,25,25,20,15), 'Skills' : []}
        else:
            return {'Name' : 'Thick White Slime', 'Level_min' : 5, 'Level_max' : 10, 'Sprite' : None, 'Stats' : (15,25,25,20,15), 'Skills' : ['Zenith']}
    
    