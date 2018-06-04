#!/usr/bin/env python3
#By A_Asaker 
import time
def isLeapYear(year):
    if year%4 == 0 and year%100 != 0 or year % 400 == 0 :
            return True
    else : return False

def nextDay(year, month, day):
    _31Month=[1,3,5,7,8,10,12]
    _30Month=[4,6,9,11]
    if day < 30 and month in _30Month or day < 31 and month in _31Month or month==2:
        if isLeapYear(year) and month ==2 and day == 28:
            return year, month, day + 1
        elif isLeapYear(year) and month ==2 and day == 29:
            return year, month+1, 1
        elif isLeapYear(year)==False and month ==2 and day == 28:
            return year, month + 1, 1
        else :
            return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
        
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False        

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

def test():
    test_cases = [((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print ("Test with data:", args, "failed")
        else:
            print ("Test case passed!")

#test()
def Calc():
    ny,nm,nd=int(time.strftime("%Y")),int(time.strftime("%m")),int(time.strftime("%d"))
    by,bm,bd=int(input("Your Birth Year : ")),int(input("Your Birth Month : ")),int(input("Your Birth Day : "))
    days=daysBetweenDates(by,bm,bd,ny,nm,nd)
    print("U Were Born From : ",int(round(days/365.25)), " Years")
    print("U Were Born From : ",int(round(days/365.25*12)), " Month")
    print("U Were Born From : ",days, " Days")
    print("U Were Born From : ",days*24, " Hours")
    print("U Were Born From : ",days*24*60, " Minutes")
    print("U Were Born From : ",days*24*60*60, " Seconds")
Calc() 
def after():
    x=input("Do You want To Calculate Again ?(Yes||No) : ").lower()
    if x == "yes" or x=="y":
        Calc()
        after()
    else : exit()
after()
