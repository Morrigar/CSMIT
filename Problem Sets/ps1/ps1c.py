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
highPct=float(1)
guess=float(lowPct+highPct/2)
final_savings=float(0)

def calculate_saving():
    global guess
    global annualSalary
    calc_salary=float(annualSalary)
    calculated_saving=float(0)
    for i in range(1,37):        
        calculated_saving = round(calculated_saving + (calc_salary/12)*guess,2)
        #print ('Savings at month',i,'=',calculated_saving)
        if (i/6).is_integer(): #apply semi-annual raise if necessary
            calc_salary=round(annualSalary*semiAnnualRaise,2)
           # print ('\nNew salary after raise=',calc_salary)
    return calculated_saving
    
def calculate_saving_print():
    global guess
    global annualSalary
    calc_salary=float(annualSalary)
    calculated_saving=float(0)
    for i in range(1,37):        
        calculated_saving = round(calculated_saving + (calc_salary/12)*guess,2)
        print ('Savings at month',i,'=',calculated_saving)
        if (i/6.).is_integer(): #apply annual raise if necessary
            calc_salary=round(annualSalary*semiAnnualRaise,2)
            print ('\nNew salary after raise=',calc_salary)
    return calculated_saving

def too_low_check():
    global annualSalary
    calculated_saving=float(0)
    for i in range(1,37):        
        calculated_saving = round(calculated_saving + (annualSalary/12),2)
        if (i/6.).is_integer(): #apply annual raise if necessary every 6th month
            annualSalary=round(annualSalary*semiAnnualRaise,2)
    return calculated_saving

while too_low_check()<750000:
    print ('Starting salary too low.')
    annualSalary = float(input('What is your starting annual salary? '))
        
print('Your semi-annual raise will be 7%, no more no less.')
print('Your monthly salary is ' + str(round(annualSalary/12,2))+'.')
print('This program will calculate what % of your\nsalary you must save each month.')
print('Total cost of your dream home minus a\n25% downpayment is $750,000.\n')

counter = int(0)

while abs(target-calculate_saving()) >=  10:
#print (guess)
#print ('Current rate of '+str(guess)+' gives a savings of '+str(calculate_saving()))
    if target-calculate_saving() > 0: #Guess is too low. Must raise it
        lowPct=guess
        guess=float((lowPct+highPct)/2)
        counter +=1
    elif target-calculate_saving() < 0 : #Guess is too high. Must lower it
        highPct=guess
        guess=float((lowPct+highPct)/2)
        counter +=1
    else :
        print('Left loop')
        break

final_savings=round(calculate_saving(),2)
        
print ('After '+str(counter)+' guesses the program determined that')
print ('if you save '+str(round((guess)*100,4))+'% of your monthly savings you')
print ('will end up with '+str(final_savings)+' dollars')
print ('after 36 months.')

#print (abs(target - calculate_saving())) #print ('Final savings after 36 months:',calculate_saving_print(guess))    

#print ('Percent savings was:',guess)