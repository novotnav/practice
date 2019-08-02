name = input("Tell me your name: ")
age = input("Tell me your age in years: ")
bday = input("Have you had your birthday this year? y for yes, n for no: ")
age = int(age)
import datetime
now = datetime.datetime.now()

yyear = now.year - age + 100
nyear = yyear - 1

if bday is "y":
    print(str(name) + ", you will turn 100 in the year " + (str(yyear)))
if bday is "n":
    print(str(name) + ", you will turn 100 in the year " + (str(nyear)))
