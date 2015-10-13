#!/usr/bin/python

game_start = raw_input('Think of a number between 100 and 0, and I will try to guess it. Hit [Enter] to start.')

guesses_taken = 0

number_guess = 50

while guesses_taken < 100:
   guess = raw_input('is it ' + str(number_guess) + '(yes/no/quit)? ')

   guesses_taken += 1

   if guess == 'no':
      higher_or_lower = raw_input('is it higher or lower than ' + str(number_guess) + ' ? ')
      if higher_or_lower == 'lower':
         number_guess = number_guess/2 
      elif higher_or_lower == 'higher':
         number_guess = 50 + (number_guess/2)
      else:
         print 'please type higher or lower '
   elif guess == 'yes':
      print 'I knew it!'
      break
   elif guess == 'quit':
      print 'bummer, I will guess your number next time!'
      break
   else:
      break
