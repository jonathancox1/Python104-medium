#convert user input of string and stretch vowels out x5
#ex Good => Goooood Alabama => Aaaaalaaaaabaaaaamaaaaa


#prompt user for input (string)
user_input = input('Give me a word: ')



#loop thorough each letter in the word
#if letter is a vowel, a e i o u
#repeat that letter 5 times

i = 0


while i < len(user_input):
    if (user_input[i - 1]) == user_input[i]:
        pass
        if user_input[i] == 'a' or user_input[i] == 'e' or user_input[i] == 'i' or user_input[i] == 'o' or user_input[i] == 'u':
            print(user_input[i] * 5, end='')
    else:
        print(user_input[i], end='')
    i += 1

print('')
