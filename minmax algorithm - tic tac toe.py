from clases import borad
from player2 import player as player2
import math
c='o'
p='x'
human=player2(p)
com=player2(c)
bord = borad(c,p)
bord.show()



print('player='+p+'  com='+c)
while 1:
    x=input('inter x \n')
    y=input('inter y\n')
    w=bord.change(human,(int(x),int(y)))
    
    
    if w is not None:
        if w==1:
            print('conputer won')
        elif w==-1:
        
            print('player won')
        elif w==2:
            continue
        else:
            print('tie')
        break

    
    (s,pp,dd)=com.best_move(bord) 
    big_score=-1000
    index=0
    for i in range(len(s)):
        if s[i]>big_score:
            big_score=s[i]
            index=i
            
            
    print('\n\n')    
    print('minimax information :')
    print(s)
    print(dd)
    print('============================')
    
    w=bord.change(com,(pp[index][0],pp[index][1]))
    bord.show()
    if w is not None:
        if w==1:
            bord.show()
            print('conputer won')
        elif w==-1:
            bord.show()
            print('player won')
        else:
            bord.show()
            print('tie')
        break
  
    
                