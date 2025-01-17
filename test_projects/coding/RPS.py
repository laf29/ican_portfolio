
from random import randint
loop = int(1)
print ("Rock Paper Scissors agiant Computer\n")
while loop == 1:
  player = input('Rock(r), paper (p), scissors (s) or quit(q)?')
  
  if player == 'q':
    loop = 0
  else:
    chosen = randint(1,3)
  
    if chosen == 1:
      computer = 'r'
    elif chosen == 2:
      computer = 'p'
    else:
      computer = 's'
  
    print player, 'vs', computer

    if player == computer:
      print 'TIE!'
    elif player == 'r' and computer == 's':
      print 'Human player wins!'
    elif player == 'r' and computer == 'p':
      print 'Computer wins!'
    elif player == 'p' and computer == 's':
      print 'Computer wins!'
    elif player == 'p' and computer == 'r':
      print 'Human player wins!'
    elif player == 's' and computer == 'r':
      print 'Computer wins!'
    elif player == 's' and computer == 'p':
      print 'Human player wins!'