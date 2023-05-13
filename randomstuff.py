import random
import sys
import time

password = ""

message1 = "A new and improved Password Generator!"
for char in message1:
  sys.stdout.write(char)
  sys.stdout.flush()
  time.sleep(0.07)
print("")
print("")
message2 = "We use your phone number digits to make it more unique to the user."
for char in message2:
  sys.stdout.write(char)
  sys.stdout.flush()
  time.sleep(0.06)
print("")
print("")
numb = input("What is the last 4 digits of your phone number? ")

print("")
print("")
for i in range(3):
    i = chr(random.randint(65, 90))
    j = chr(random.randint(65, 90)).lower()
    password = str(password) + i + j

message3 = "You're newly generated password is: "
for char in message3:
  sys.stdout.write(char)
  sys.stdout.flush()
  time.sleep(0.06)
print("")
print("")
n = len(password)
counter = 0
new_password = ''
for k in range(0,n):
  if counter != 4:
    letter = password[k:]
    new_password += letter[k:]
    new_password += numb[k:]
    counter += 1
print(str(new_password))
print("")
feedback = input("Was this helpful? yes or no (Please no capitalization): ")
yes = "yes"
print("")

if (feedback == yes):
    print("")
    print("Thank you, I'm glad that this helped! :) ")

else:
    print("I'm sorry that this didn't help. If you have any suggestion or feedback, please go to the feedback program I created in Projects.")