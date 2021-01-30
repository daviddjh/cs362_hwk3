# By David Headrick
#
# Instructions:
# Using python3, run this file
# Enter only the year you'd like to check, then press enter
#

# User Input:

year = input("Enter a year to calculate if it is a leap year: ")
year = int(year)

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

