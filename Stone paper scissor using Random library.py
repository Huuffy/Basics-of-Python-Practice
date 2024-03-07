import random

ps=0
cs=0
tie=0

while True:
    print("\nstone\npaper\nscissor\npress q to exit")
    
    pch=input('enter your choice: ')
            
    if pch=='q':
        print('\ni liked to play with you')
        break
    if not(pch=='stone' or pch=='paper' or pch=='scissor'):
        print(' \n \ncheck your input')
        continue


    rch=random.randint(1,3)
    if rch==1:
              cch='stone'
    elif rch==2:
              cch='paper'
    else:
        rch==3
        cch='scissor'
    print(pch,cch)
    if pch==cch:
        print('its a clash')
        tie+=1
    elif (pch=='stone' and cch=='scissor') or (pch=='paper' and cch=='stone') or (pch=='scissor' and cch=='paper'):
        print('hurray you won')
        ps+=1
    else:
        print('better luck next time')
        #can make opposite for computer
        cs+=1
    print('win / lose / tie score')
    print(ps,'/',cs ,'/',tie)
    print('\n \nnext round')
print('\nfinal score \n win=',ps,'lose',cs,'ties',tie)

























