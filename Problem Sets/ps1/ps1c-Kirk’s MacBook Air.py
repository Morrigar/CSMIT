#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 20:33:27 2017

@author: ksripinyo
"""
#    Function to caculate over 36 months
annualSalary = float(input('What is your starting annual salary? '))
#Set variables here
target=float(750000)
semiAnnualRaise=float(1.07)
investmentReturn=float(1.04)
lowPct=float(0) #The annual return rate on savings.
highPct=float(100)
guess=float((lowPct+highPct/2)*0.01)

def calculate_saving(guess):
    global annualSalary
    currentSavings=float(0)
    for i in range(1,37):        
        currentSavings = round(currentSavings + (annualSalary/12)*guess,2)
        #print ('Savings at month',i,'=',currentSavings)
        if (i/6.).is_integer(): #apply annual raise if necessary
            annualSalary=round(annualSalary*semiAnnualRaise,2)
            #print ('\nNew salary after raise=',annualSalary)
    return currentSavings

def calculate_saving_print(guess):
    global annualSalary
    currentSavings=float(0)
    for i in range(1,37):        
        currentSavings = round(currentSavings + (annualSalary/12)*guess,2)
        print ('Savings at month',i,'=',currentSavings)
        if (i/6.).is_integer(): #apply annual raise if necessary
            annualSalary=round(annualSalary*semiAnnualRaise,2)
            print ('\nNew salary after raise=',annualSalary)
    return currentSavings

while calculate_saving(1.0)<750000:
    print ('Starting salary too low.')
    annualSalary = float(input('What is your starting annual salary? '))
        
print('Your semi-annual raise will be 7%, no more no less.\n')
print('Your monthly salary is',round(annualSalary/12,2),'.\n')
print('This program will calculate what % of your\nsalary you must save each month.')
print('Total cost of your dream home minus a\n25% downpayment is $750,000.\n')


print ('Guess=',guess)

while abs(target-calculate_saving(guess)) > 100:
    if target-calculate_saving(guess) > 0: #Guess is too low. Must raise it
        lowPct=guess*100
        guess=float((lowPct+highPct/2*0.01))
    if target-calculate_saving(guess) < 0: #Guess is too high. Must lower it
        highPct=guess*100
        guess=float((lowPct+highPct/2*0.01))   
        
print ('Final savings after 36 months:',calculate_saving_print(guess))    

print ('Percent savings was:',guess)