#!/usr/bin/python3
# home/shon/workspace/comptime.py
# by Shon Garrison
# Created on: Aug 1, 2012
# Updated on: April 20, 2021

import os

globalBank = 0.0
globalPreview =""

def quit():
    print("\n")
    print("Application is Now Exiting...")

def get_Date():
    year, month, day = widget.get_date()
    self.lblCurDate.set_text(str(month + 1) + "/" + str(day) + "/" + str(year))
    
def on_clear():
    print("\n")
    print("Now Clearing Form...")

def on_calc():
    global globalBank
    global globalPreview
    print("\n")
    print("Calculating New Daily Bal...")
    #sets up variables and gets Earned or Taken Values
    #date = self.lblCurDate.get_text()
    #calcearned = self.entryEarned.get_text()
    #calctaken = self.entryTaken.get_text()
    #preview = self.combobox1.get_active_text()
    #taken = self.entryTaken.get_text()
    #bank = globalBank
    
    #If Earned is blank, it will be set to zero, otherwise it gets Earned
    #entry
    if calcearned == "":
        calcearned = 0.0
    else:
        calcearned = self.entryEarned.get_text()
    #if Taken is blank, it will be set to zero, otherwise it gets Taken
    #entry
    if calctaken == "":
        calctaken = 0.0
    else:
        calctaken = self.entryTaken.get_text() 
    #convert string variables to decimal(float) for calculation
    calcearned = float(calcearned) * 1.5
    calctaken = float(calctaken)
    newbal = calcearned - calctaken
    newbank = newbal + float(bank)
    #convert to back to string to display in label
    newbal = str(newbal)
    newbank = str(newbank)
    print("\n")
    print("Setting Preview of New Balance Applied...")
    #shows current calculation daily balance
    #self.lbl6.set_text(newbal)
    
    
    #shows current preview of time entry prior to writing text file
    self.lblPreview.set_text("Total time to enter on affidavit = " 
    + newbal + " hrs\n" + "-"*145 + "\n" + "Date" + " "*25 + "Reason"
    + " "*25 + "Earned" + " "*25 + "Taken" + " "*25 + "New Balance\n"
    + "-"*9 + " "*24 + "-"*12 + " "*25 + "-"*12 + " "*25 + "-"*10
    + " "*25 + "-"*21 + "\n" + str(date) + " "*13 + str(preview)
    + " "*25 + str(calcearned) + " "*40 + str(taken) + " "*30
    + newbank)

    globalPreview = (str(date) + " "*8 + str(preview) 
    + " "*10 + str(calcearned) + " "*18 + str(taken) + " "*17 
    + newbank + "\n"
    + "-"*90 + "\n")

def on_apply():
    global globalBank #access global variable
    print("\n")
    print("Applying New Daily Balance to Bank...")
    
    #incorporate to opening file
    bank2 = globalBank
    newDaybal= self.lbl6.get_text() #get daily balance text
    newbank2 = float(newDaybal) + bank2
    
    globalBank = (newbank2) #update global variable with new balance
    newbank2 = str(newbank2) #convert to string to put into label and file
    #self.lbl5.set_text(newbank2) #put in bank label
    
    #writes to the bankfile
    f = open("/home/sgarrison/temp/test1.txt", "w")
    f.write(newbank2)
    f.close()
    
    #writes to runfile
    f2 = open("/home/sgarrison/temp/test2.txt", "a")
    f2.write(globalPreview)
    f2.close()
    
    
    self.on_clear(widget)


#start program
print("Comptime Calculator")
print("---------------------------------------------------------------")


#creates the applicable buttons
#self.btnClear = gtk.Button("Clear")
#self.btnCalc = gtk.Button("Calculate")
#self.btnApply = gtk.Button("Apply")
#self.btnClose = gtk.Button("Exit")


#pulls bank amount from text file and loads it for globalBank 
#global globalBank

#checks to see if the bankfile exists.  If it does, it pulls from it.
if os.path.isdir("/home/sgarrison/temp/") and os.path.isfile("/home/sgarrison/temp/test1.txt"):
    f = open("/home/sgarrison/temp/test1.txt", "r")
    text = f.readline()
    globalBank = float(text)        
    f.close()
    
else:
    #if bankfile dosen't exist, it creates it with a 0.0 balance then
    #reads from it.
    startBal = "0.0"
    f = open("/home/sgarrison/temp/test1.txt", "w")
    f.write(startBal)
    f.close()
    
    f = open("/home/sgarrison/temp/test1.txt", "r")
    text = f.readline()
    globalBank = float(text)        
    f.close()
    
    f = open("/home/sgarrison/temp/test2.txt", "w")
    f.write("Orange County Juvenile Probation Dept.\n"
    + "-"*40 + "\n" 
    + "Personal Comptime Sheet for: Shon Garrison\n"
    + "\n" 
    + "Date" + " "*13 + "Reason" + " "*11 + "Earned" + " "*16 
    + "Taken" + " "*15 + "New Balance\n"
    + "-"*9 + " "*7 + "-"*12 + " "*6 + "-"*7 + " "*15 
    + "-"*6  + " "*14 + "-"*12 + "\n")


print("Your Current Balance is " + str(globalBank))





#creates the applicable labels
#self.lblPreview = gtk.Label("Preview")
#self.lbl7 = gtk.Label("Current Date Selected:")
#self.lblCurDate = gtk.Label("Select Activity Date")
#self.lblCase = gtk.Label("Case / Reason:")
#self.lbl1 = gtk.Label("hrs")
#self.lblEarned = gtk.Label("Earned")
#self.lblTaken = gtk.Label("Taken")
#self.lbl2 = gtk.Label("hrs")
#self.lbl3 = gtk.Label("Bank:")
#self.lbl5 = gtk.Label(text)
#self.lbl4 = gtk.Label("Daily Total:")
#self.lbl6 = gtk.Label("0.0")


#creates the list for the combobox
#self.combobox1.append_text("[Enter One]")
#self.combobox1.append_text("On-Call")
#self.combobox1.append_text("Det Visit")
#self.combobox1.append_text("Special Grp")
#self.combobox1.append_text("Transport")
#self.combobox1.append_text("Program")
#self.combobox1.append_text("Personal")
#self.combobox1.append_text("Sick")

quit()


