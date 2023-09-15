sData = {}
global sHealth, sMana
sHealth = 0
sMana = 0
counter = 0
barrier = 10

#Level Checker and level up
def leveler():
    barrier = 10
    for i in range(sData['Level'] - 1):
        barrier = (barrier * 1.5) // 1
        if sData['Exp'] >= barrier:
            sData['Level'] = int(sData[0]) + 1
            print('''
            
█░░░█▀▀░█░█░█▀▀░█░░░░█░█░█▀█░░█
█░░░██░░█░█░██░░█░░░░█░█░█    █░░█
█▄▄░█▄▄░▀▄▀░█▄▄░█▄▄░░█▄█░█▀▀░░▄

''')
            t(1.5)
            print(f"You are now Level: {sData[Level]}")
            t()
            
#Player details in interface
#format
#Lvl,Name,Exp, Crystals,Class,Health,Mana,Vitality,Power,Wisdom,Dexterity
#Sense, Allocatable stat points
# { Name : name, Level : 1, Exp : 1, Stats: 0, Crystals : 0, Vit : 10, Str : 10, Wis : 10, Dex : 10, Sen : 10, Items : [], Skills : [] }

def PD():
    leave_line = ('= ' * 48)
    print(leave_line)
    Max_HP, Max_Mana = sData['Vit'] * 10, sData['Wis'] * 10
    print(f'''
    \t Name:    {sData['Name']} \t Crystals:    {sData['Crystals']} \t\t HP:    {sHealth}/{Max_HP}
    \t Lvl:    {sData['Level']} \t\t Exp:    {sData['Exp']} / {barrier} \t\t Mana: {sMana}/{Max_Mana}\n''')
    print(leave_line)
    
def heal():
    global sHealth, sMana
    Max_HP, Max_Mana = sData['Vit'] * 10, sData['Wis'] * 10
    print(Max_HP, Max_Mana)
    x,y = sHealth, sMana
    sHealth = Max_HP
    sMana = Max_Mana
    return x,y
    
def mG_win(rank, multiplier = 1):
    temp = rank.lower()
    cash = sData['Crystals']
    p = 10000
    if temp == 'f':
        p = 10
    elif temp == 'd':
        p = 100
    sData.update({'Crystals' : cash + p* multiplier})
    print(f"You've earned {p} crystals!")
    