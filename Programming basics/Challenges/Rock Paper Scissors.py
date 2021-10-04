import random
computer_choice = ['rock','paper','scissors']
die_num = random.randint(0,2)

print("do you choose:")
print("1: rock")
print("2: paper")
print("3: scissors")
choice = int(input())
r_choice = choice - 1
while choice > 3 or choice < 1: ### SRC - Good use of validation
    print("invalid input, please input a number between 1 and 3")
    choice = int(input())
#endwhile
print("the computer has chosen:", computer_choice[die_num])

if r_choice != die_num:
    if r_choice + die_num == 1 and r_choice > die_num:
        print("you win")
    else: 
        print("you lose")
    #end if
    if r_choice + die_num == 2 and r_choice > die_num:
        print("you lose")
    else:
        print("you win")
    #end if
    if r_choice + die_num == 3 and r_choice > die_num:
        print("you win")
    else:
        print("you lose")
    #end if
else:
    print("you draw")
#end if