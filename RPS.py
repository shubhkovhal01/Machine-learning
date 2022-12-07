import random
from re import S
def game(comp,you):
    if comp==you:
        return None
    if comp=="P":
        if you=="R":
            return False
        elif you=="S":
            return True
    if comp=="P":
        if you=="S":
            return False
        elif you=="R":
            return True
    if comp=="R":
        if you=="S":
            return False
        elif you=="P":
            return True
   



randno=random.randint(1,3)

print("coomputer turn : rock(R),paper(P)or ,scissor(S)")
if randno==1:
    comp= 'R'
if randno==2:
    comp= 'P'
if randno==3:
    comp= 'S'    

you=input("Your turn :rock(R),paper(P)or ,scissor(S) ? : ")
print(f"comp enter:{comp}")
print(f"You entered:{you}")

s=game(comp,you)
if s==None:
    print("Game is tie")
elif s:
    print("you win")
else:
    print("You lose")