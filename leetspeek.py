#convert user input to 'leetspeak'
# A -> 4
# E -> 3
# G -> 6
# I -> 1
# O -> 0
# S -> 5
# T -> 7


#ask user for input
input = str(input("Give me your text: "))
user_input = input.upper()


#define function to check which letter is a leet letter
def convert(a):
    if a == 'A':
        return '4'
    elif a == 'E':
        return '3'
    elif a == 'G':
        return '6'
    elif a == 'I':
        return '1'
    elif a == 'O':
        return '0'
    elif a == 'S':
        return '5'
    elif a == 'T':
        return '7'
    else:
        return a


#loop throught the indexes to determin if the character needs to be changed
for letter in user_input:
    leeted = convert(letter)
    print(leeted, end='') #prints a % at the end of the line???????????
