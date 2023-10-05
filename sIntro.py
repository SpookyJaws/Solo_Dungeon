#Game Title Screen
import sFuncs as sf
import sLogin

text='\t\t\t\t\tA Text - Based RPG'
text2='''
    
\t\t\t\t░██████████╗░███████╗░██╗░░░░░░░░░███████╗░
\t\t\t\t██╔════════╝██╔════██╗██║░░░░░░░░██╔════██╗
\t\t\t\t╚█████████╗░██║░░░░██║██║░░░░░░░░██║░░░░██║
\t\t\t\t░╚═══════██╗██║░░░░██║██║░░░░░░░░██║░░░░██║
\t\t\t\t██████████╔╝╚███████╔╝██████████╗╚███████╔╝
\t\t\t\t╚═════════╝░░╚══════╝░╚═════════╝░╚══════╝░
'''
def Int(x=None):
    sf.clr()
    print(text2)
    flag=0
    if x != None:
        for i in range(5):
            flag=1
            if i%2==0:
                sf.clr(0)
                print(text2)
                print(text)
                sf.t(0.3)
            else:
                sf.clr(0)
                print(text2)
                sf.t(0.3)
    else:
        sf.printer(text,'',0.1)
    if flag==1:
        sLogin.Logger()
def Start():
    Int()
    print('= '*50)
    sf.printer('\t\t\t\t    Press Enter to continue:')
    sf.t(1)
    input()
    Int(5)