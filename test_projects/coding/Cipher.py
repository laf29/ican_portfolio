loop = int(1)
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabetA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
while loop == 1:
  print 'Caesar Cipher Encrypter/Decrypter\n\n'
  print "By Liam Farrell\n\n"
  print "Please pick which option you would like:"
  print "0: Quit"
  print "1: Encrypter"
  print "2: Decrypter"
  opt = input("Enter your option:")
  if opt == '1':
    key = int(input('Enter the key number (usally 3): '))
    newMessage = ''

    message = input('Please enter a message: ')

    for character in message:
      if character in alphabet:
        position = alphabet.find(character)
        newPosition = (position + key) % 26
        newCharacter = alphabet[newPosition]
        newMessage += newCharacter
      elif character in alphabetA:
        position = alphabetA.find(character)
        newPosition = (position + key) % 26
        newCharacter = alphabetA[newPosition]
        newMessage += newCharacter
      else:
        newMessage += character
    print 'Your new message is: "',newMessage,'"\n\n'
    print '###########################################################\n\n'
 
  elif opt == '2':
    key = int(input('Enter the key number (usally 3): '))
    newMessage = ''
    message = input('Please enter a encrypted message: ')
    for character in message:
      if character in alphabet:
        position = alphabet.find(character)
        newPosition = (position - key) % 26
        newCharacter = alphabet[newPosition]
        newMessage += newCharacter
      elif character in alphabetA:
        position = alphabetA.find(character)
        newPosition = (position - key) % 26
        newCharacter = alphabetA[newPosition]
        newMessage += newCharacter
      else:
        newMessage += character
    print 'Your decoded message is: "',newMessage,'"'
    print '\n###########################################################\n\n'
        
        
  elif opt == '0':
    print "Exiting..."
    loop = 0
  else:
    print "Invalid option, try again."
    print '\n###########################################################\n\n'


###############################################################################

#alphabet = 'abcdefghijklmnopqrstuvwxyz'
#alphabetA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#key = int(input('Enter the key number: '))
#newMessage = ''

#message = input('Please enter a message: ')

#for character in message:
#  if character in alphabet:
#    position = alphabet.find(character)
#    newPosition = (position + key) % 26
#    newCharacter = alphabet[newPosition]
#    #print ('The new character is ', newCharacter)
#    newMessage += newCharacter
#else:
#  newMessage += character
#print ('Your new message is ', newMessage)