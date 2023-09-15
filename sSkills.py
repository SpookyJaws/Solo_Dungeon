#All skills will be stored here
#
#
#
#
#
from random import randint

#code for returning random skill
#parameter : list of skills

def skills(Items):
    Length = len(Items)
    Skill_no = None
    if Length != 0:
        Krill = randint(0, Length - 1)
        Skill_Name = Items[Krill]
        Skill = Skill_Data(Skill_Name.lower())
        return Skill
    else:
        return None

# modifiers
# eDamage_temp (x) - Temporary attack stat multiplied by x
# pDefense (x) - 

def Skill_Data(n):
    if n[0] == a:
    if n[0] == b:
    if n[0] == c:
    if n[0] == d:
    if n[0] == e:
    if n[0] == f:
    if n[0] == g:
        if n == 'gooblin':
            #Damage Multiplied by 0.5
            #User defense modifier reduced by 0.1
            return {'eDamage_temp' : 0.5, 'pDefense' : 0.1, 'Text' : "You get bombarded by green goo"}
    if n[0] == h:
    if n[0] == i:
    if n[0] == j:
    if n[0] == k:
    if n[0] == l:
    if n[0] == m:
    if n[0] == n:
    if n[0] == o:
    if n[0] == p:
    if n[0] == q:
    if n[0] == r:
    if n[0] == s:
        if n == 'slam':
            #Damage Multiplied by 1.2
            return {'eDamage_temp' : 1.2}
    if n[0] == t:
    if n[0] == u:
    if n[0] == v:
    if n[0] == w:
    if n[0] == x:
    if n[0] == y:
    if n[0] == z:
        if n == 'zenith':
            #Damage Multiplied by 0.75
            #You have a 50% chance to get stunned
            return {'Text' : "The enemy starts glowing white and finally... \n\nIt bursts out thick white liquid all over your body", 'eDamage_temp' : 0.75, 'Stun' : 0.5}
            #

    
    
