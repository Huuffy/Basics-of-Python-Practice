#legth gives length of area

area=[' ',' ',' ',' ',' ',' ',' ',' ',' ']

#print(len(area))

symbol='X'
#round  to reduce decimal point/round off
rounds=0
#winner=''
while True:
    print('  ',area[6],'|',area[7],'|',area[8],'  ')
    print('  ___|___|___')
    print('  ',area[3],'|',area[4],'|',area[5],'  ')
    print('  ___|___|___')
    print('  ',area[0],'|',area[1],'|',area[2],'  ')
    print('     |   |   ')
    print('this is',symbol,' s turn')
    print('\n')
    player1=int(input('enter the position : '))
    if area[player1-1]!=' ':
        print('do not overwrite \n')
        continue
    else:
        area[player1-1]=symbol
        rounds+=1
    area[player1-1]=symbol
    rounds+=1
    if symbol=='X':
        symbol='O'
    else:
        symbol='X'
    if rounds>4:
#range-(start,end,add with)
        #or(
        for i in range(0,7,3):
            if area[i]==area[i+1] and area[i+2]==[i] and area[i]!=' ':
                print('yay',symbol,'won')
                
                #or winner=area[i]
                
        for i in range(0,3,1):
             if area[i]==area[i+3] and area[i+6]==[i] and area[i]!=' ':
                 print('yay',symbol,'won')
                 
                  #or winner=area[i]
        if area[0]==area[4] and area[0] == area[8]:
             print('yay',symbol,'won')
             score+=1
             #winner=area[0]
        if area[2]== area[4] and area[2] == area[6]:
             print('yay',symbol,'won')
             
             #winner=area[2]   
                
                 
             #if winner:
                # print(winner,'is winner')
               #  break
            
    if rounds==9:
        print('  ',area[6],'|',area[7],'|',area[8],'  ')
        print('  ___|___|___')
        print('  ',area[3],'|',area[4],'|',area[5],'  ')
        print('  ___|___|___')
        print('  ',area[0],'|',area[1],'|',area[2],'  ')
        print('     |   |   ')
        print('\n')
        print('draw ughhhhhh')
        break
    
#add score and make it as per number line in pc
#make chosable rounds
#dont allow over write
#pass - do not check here just check till above line
    
