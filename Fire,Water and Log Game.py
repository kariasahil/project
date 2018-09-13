#!/bin/python3

from random import randint

print('FIRE,WATER and LOG GAME!')
name=input('What is your name?')
game=input('Choose any one initials from the following Fire(f),Water(w),Log(l):')
print(game,' vs ', end=' ')
choosen= randint(1,3)
#print(choosen)

if choosen==1:
  computer='f'
  
elif choosen==2:
  computer='w'
  
else:
  computer='l'
  
print(computer)
  
if game == 'f' and computer == 'f':
   print('Draw')
  
elif game == 'f' and computer == 'w':
   print('Computer Wins!')
  
elif game == 'f' and computer == 'l':
   print(name,'Wins!')
   
elif game == 'w' and computer == 'w':
   print('Draw')
  
elif game == 'w' and computer == 'l':
   print('Computer Wins!')
  
elif game == 'w' and computer == 'f':
   print(name,'Wins!')
   
elif game == 'l' and computer == 'l':
   print('Draw')
  
elif game == 'l' and computer == 'f':
   print('Computer Wins!')
  
elif game == 'l' and computer == 'w':
   print(name,'Wins!')
  



