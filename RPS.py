from numpy import random 
plyer = 0
pc = 0
while plyer < 3 and pc < 3:
    pc_choice = random.choice(['rock' , 'paper' , 'scissors'])
    plyr_choice = input('Choose one : (rock , paper , scissors) :')
    print('you :'+plyr_choice)
    print('me :'+pc_choice)
    if pc_choice == plyr_choice :
        print("************************") 
        
    elif pc_choice == 'paper' and plyr_choice == 'rock' \
    or pc_choice == 'rock' and plyr_choice == 'scissors'\
    or pc_choice == "scissors" and plyr_choice == 'paper':
        print("************************")
        pc += 1

    elif pc_choice == 'rock' and plyr_choice == 'paper'\
    or pc_choice == 'scissors' and plyr_choice == 'rock'\
    or pc_choice == 'paper' and plyr_choice == 'scissors' :
        print("************************")
        plyer +=1

    else :
        print("what is this ? pleas chose currect")

    print('me:'+str(pc)+'\t you:'+str(plyer))
if pc > plyer :
    print("*** hahaha yesss i winnn ***")
else :
    print("*** ohh nooo you won ***")