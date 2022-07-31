### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
# Requires a == for equals to.
# Missing a : after the else 



  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2

# dif has been used instead of def. 
# card1 and card2 should be separated by commas. 
# card has not been defined, should be card1 or card2
# Indentation on the if statement is incorrect (should be more indented)

def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
# Total has not been assigned a value prior to the for loop. 
# The return statement is within the for loop (also the indentation is too far in). 
# The string in the return is not bracketed
# Can't concatenate the string and total anyway, needs to be formatted string. 