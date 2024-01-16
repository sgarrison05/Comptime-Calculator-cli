#!/usr/bin/python3
# by Shon Garrison
# Created on: Aug 1, 2012
# Updated on: January 2024

import os
from datetime import date
import users as nu

gBank = 0.0
gPreview = ""
gDaily_Bank = 0.0
running = True
gname = ''
gposition = ''


def quit():
    print()
    print("Application is Now Exiting...")
    exit()


def get_Date():
    # get the date for the current transaction
    today = date.today()
    print()
    answer = input("Do you have a date to enter? (y=enter date, n=today) \n")

    if answer == "y":
        m = int(input("Enter Month \n"))
        d = int(input("Enter Day \n"))
        y = int(input("Enter Year (YYYY) \n"))

        d1 = date(y, m, d)
        d1 = d1.strftime("%m/%d/%Y")

    else:
        d1 = today.strftime("%m/%d/%Y")

    return d1


def on_calc(cearned, ctaken, reason):
    global gPreview  # Access to global variable
    global gBank

    # sets up variables and gets Earned or Taken Values
    bank = gBank
    dte = get_Date()

    print()
    print("Calculating New Daily Balance...")
    print()

    # convert string variables to decimal(float) for calculation
    cearned = float(cearned) * 1.5
    ctaken = float(ctaken)
    newbal = cearned - ctaken
    newbank = newbal + float(bank)
    gBank = str(newbank)

    # convert to back to string to display in label
    newbal = str(newbal)
    newbank = str(newbank)
    print()
    print("Setting Preview of New Balance Applied...")
    print()
    print()

    # shows current preview of time entry prior to writing text file
    print("Total time to enter on affidavit = " + newbal + " hrs\n"
          + "-" * 100 + "\n"
          + "Date" + " " * 18 
          + "Reason" + " " * 16 
          + "Earned" + " " * 18 
          + "Taken" + " " * 17 
          + "Balance\n"
          + "-" * 10 + " " * 12 + "-" * 10 + " " * 12 
          + "-" * 12 + " " * 12 + "-" * 10
          + " " * 12 + "-" * 10 + "\n" 
          + str(dte) + " " * 12 
          + "{:11s}".format(reason) + " " * 12
          + "{:5s}".format(str(cearned)) + " " * 19 
          + "{:5s}".format(str(ctaken)) + " " * 18
          + newbank + "\n"
          + "-" * 100) 
    print()

    # What gets put into run file on applying calc
    gPreview = (str(dte) + " " * 7 
                + "{:11s}".format(reason) + " " * 12 
                + "{:5s}".format(str(cearned)) + " " * 19                 
                + "{:5s}".format(str(ctaken)) + " " * 18
                + newbank + "\n"
                + "-" * 100 + "\n")


def on_apply():
    global gBank  # access global variable
    global gPreview
    print()
    print("Applying New Daily Balance to Bank...")
    print()

    # incorporate to opening file
    bank2 = float(gBank)
    newDaybal = float(gDaily_Bank)  # get daily balance text
    newbank2 = float(newDaybal) + bank2

    gBank = (str(newbank2))  # update global variable with new balance
    newbank2 = str(newbank2)  # convert to string to put into label and file

    # writes to runfile
    f2 = open("D:/Temp/test2.txt", "a")
    f2.write(gPreview)
    f2.close()

# ====================================================================================
    
# start program
print()
print("Comptime Calculator")
print("---------------------------------------------------------------")

# checks to see if the bank file exists.  If it does, it pulls from it.
if os.path.isdir("D:/Temp/") and os.path.isfile("D:/Temp/test2.txt"):
    f = open("D:/Temp/test2.txt", "r")
    my_list = []
    for line in f:
        for char in line:
            if char[-1] == "\n" and line.__contains__("/"):
                t = float(line[-7:-1].lstrip(" "))
                my_list.append(t)
    gBank = my_list[-1]
    f.close()

else:
    # if bank file doesn't exist, it creates it with a 0.0 balance then
    # reads from it.
    gBank = float("0.00")
    dte_today = date.today()
    d2 = dte_today.strftime("%m/%d/%Y")
    gname = input("What is your name? ")
    print()
    print("Examples are Chief, JPO, or Staff")
    gposition = input("What is your position? ")

    match gposition:
        case "Chief":
            gname = nu.Chief(gname)
        case "JPO":
            gname = nu.JPO(gname)
        case "Staff":
            gname = nu.Staff(gname)
        case _:
            print("That position does not exist!")
            print("Cannot create bankfile.")
            quit()
            running = False

    # Creates running file skeleton
    f = open("D:/Temp/test2.txt", "w")
    f.write(nu.User.CompanyName +"\n"
            + "-" * 40 + "\n"
            + "Personal Comptime Sheet for: " + str(gname.name) + ", " + str(gname._title) + "\n"
            + "\n"
            + "Date" + " " * 14 
            + "Reason" + " " * 16 
            + "Earned" + " " * 18 
            + "Taken" + " " * 17 
            + "New Balance\n"
            + "-" * 10 + " " * 7 + "-" * 10 + " " * 12  
            + "-" * 12 + " " * 12 + "-" * 10
            + " " * 13 + "-" * 14 + "\n"
            + str(d2) + " " * 7
            + "Placeholder" + " " * 12
            + "{:5s}".format("0.00") + " " * 19 
            + "{:5s}".format("0.00") + " " * 18
            + str(gBank) + "\n"
            + "-" * 100 + "\n")
    f.close()

while running:
    print()
    print("Your Current Balance is " + str(gBank))
    print()
    print("---------------------------------------------------------------")
    print()

    print("What do you want to do?\n")
    print("1.) Add a transaction")
    print("2.) Exit\n")
    choice = int(input())

    if choice == 1:
        print()
        print("Type of Transaction\n")
        print("1. Earned (+)")
        print("2. Taken (-)\n")
        transaction = int(input())

        if transaction == 1:
            print()
            print("Examples include -- On-Call, Det Visit, Special Grp, Transport, Program, or you may write your own.")
            reason = input("Reason for earned time?\n")
            reason = reason.ljust(11, " ")
            print()
            earned = str(input("Enter time in \"0.00\" format\n"))
            taken = float(0.00)
            on_calc(earned, taken, reason)
            on_apply()

        else:
            print()
            print("Examples include -- Sick, Personal, or you may write your own.")
            reason = str(input("Reason for time taken?\n"))
            reason = reason.ljust(11, " ")
            print()
            taken = str(input("Enter time in \"0.00\" format\n"))
            earned = float(0.00)
            on_calc(earned, taken, reason)
            on_apply()

    else:
        quit()
        running = False
