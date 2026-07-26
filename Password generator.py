# I have made the program just to generate a strong password
import random #First we have to import random and import strings
import string
# Rather than collecting every character you should do it all rather than collecting every one in the sets

characters = string.ascii_letters + string.digits + string.punctuation
# Here"" means starting with an empty string now "".join helps in joining every character

password = "".join(random.choices(characters,k=8))

print(password)
# Remeber choice is for only single choice but choices is for multiple choices