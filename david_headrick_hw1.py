# By David Headrick
#
# Instructions:
# Using python3, run this file
# Enter only the year you'd like to check, then press enter
#

# User Input:

#while 1:

year = input("Enter a year to calculate if it is a leap year: ")
try:
  year = int(year)
except ValueError:
  print("The entered value is not a valid number")
  exit()

if len(str(year)) > 4 or year < 0: 
  print("The entered value is not a valid year")
  exit()

# Logic:

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Yes, " + str(year) + " is a leap year")
    else:
      print("No, " + str(year) + " is not a leap year")
  else:
    print("Yes, " + str(year) + " is a leap year")
else:
  print("No, " + str(year) + " is not a leap year")

