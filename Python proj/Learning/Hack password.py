#password = ""


password = input("Enter a Three Letter Password: ")
import itertools

# Define the set of valid characters
valid_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

# Generate all possible combinations of valid characters of length 5


attempts = 0
combinations = itertools.product(valid_chars, repeat=3)

if str(combinations) != str(password):
          print(''.join(combinations))
          attempts += 1
print("Success!" + "   Attempts Made: " + str(attempts))    
     # elif str(key) == str(password):    

          
    
