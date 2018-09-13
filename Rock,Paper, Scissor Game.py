'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

#!/bin/python3

from random import randint 
name=input('What is your name?')
game=input('Hey! Choose any one from Rock(r),Paper(p),Scissors(s) :')
print(game ,'vs', end=' ')
choosen= randint(1,3)
#print(choosen)
if choosen==1:
  computer='r'
  
  
elif choosen==2:
  computer='p'
  
else:
  computer='s'
     
print(computer)
      
if game == computer:
  print('Draw!')
   
elif game == 'r' and computer == 'p':
  print('Computer Wins!')
  
elif game == 'r' and computer == 's':
  print(name ,'Wins!')
  
elif game == 's' and computer == 'p':
  print('Computer Wins!')
  
elif game == 's' and computer == 'r':
  print(name, 'Wins!')
  
elif game == 'p' and computer == 's':
  print('Computer Wins!')
  
elif game == 'p' and computer == 'r':
  print(name, 'Wins!')
  

