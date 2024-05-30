from random import random as rd
money=10000
for i in range(100000):
    win=0
    player_choice=int(6*rd())+1
    for j in range(3):
        dice_point=int(6*rd())+1
        if dice_point==player_choice:
            win+=1
    if win==3:
        money+=3
    elif win==2:
        money+=2
    elif win==1:
        money+=1
    else:
        money-=1
print(money)