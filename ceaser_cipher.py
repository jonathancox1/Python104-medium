#given a string print the ceaser cipeher or ROT13 of that string
#use the code to decipher the follow: "lbh zhfg hayrnea jung lbh unir yrnearq"

#letters offset by 13
#plain = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
#cipher = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
to_decipher = input('Text to decipher: ')




def ceaser(input):
    #cipher = ['a',b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
    plain = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    i = 0
    decipher = []
    while i < len(input):
        if input[i] == 'a':
            decipher.append(plain[0])
        elif input[i] == 'b':
            decipher.append(plain[1])
        elif input[i] == 'c':
            decipher.append(plain[2])
        elif input[i] == 'd':
            decipher.append(plain[3])
        elif input[i] == 'e':
            decipher.append(plain[4])
        elif input[i] == 'f':
            decipher.append(plain[5])
        elif input[i] == 'g':
            decipher.append(plain[6])
        elif input[i] == 'h':
            decipher.append(plain[7])
        elif input[i] == 'i':
            decipher.append(plain[8])
        elif input[i] == 'j':
            decipher.append(plain[9])
        elif input[i] == 'k':
            decipher.append(plain[10])
        elif input[i] == 'l':
            decipher.append(plain[11])
        elif input[i] == 'm':
            decipher.append(plain[12])
        elif input[i] == 'n':
            decipher.append(plain[13])
        elif input[i] == 'o':
            decipher.append(plain[14])
        elif input[i] == 'p':
            decipher.append(plain[15])
        elif input[i] == 'q':
            decipher.append(plain[16])
        elif input[i] == 'r':
            decipher.append(plain[17])
        elif input[i] == 's':
            decipher.append(plain[18])
        elif input[i] == 't':
            decipher.append(plain[19])
        elif input[i] == 'u':
            decipher.append(plain[20])
        elif input[i] == 'v':
            decipher.append(plain[21])
        elif input[i] == 'w':
            decipher.append(plain[22])
        elif input[i] == 'x':
            decipher.append(plain[23])
        elif input[i] == 'y':
            decipher.append(plain[24])
        elif input[i] == 'z':
            decipher.append(plain[25])
        #if not a letter must be space so print a space
        elif input[i] == ' ':
            decipher.append(' ')   

        #increment counter 
        i += 1
    x = "".join(decipher)
    print(x)
    return x

ceaser(to_decipher)