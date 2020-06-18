#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 20:33:27 2017

@author: ksripinyo
"""


# User inputted variables here
annual_salary = float(input('What is your starting annual salary? '))
semi_annual_raise = float(input('What % is your semi-annual raise? '))
portion_saved = float(input('What portion of your salary will you save each month (decimal form)? '))
total_cost = float(input('What is the total cost of your dream home? '))

#fixed variables here
portion_down_payment = float(0.25) #defined by professor
current_savings = float(total_cost*portion_down_payment)
r = float(0.04) #The annual return rate on savings.
months = int(0) #set a variable for number of months
semi_annual_raise=semi_annual_raise/100

while months < 37:
    current_savings = round(current_savings + current_savings*(r/12) + (annual_salary/12)*portion_saved,2)
    print ('Savings at month',months,'=',current_savings)
    months = months +1
    if (months/6.).is_integer():
        annual_salary=round(annual_salary*(1+semi_annual_raise),2)
        print ('\nNew salary after raise=',annual_salary)
        
print ('Total savings at',months,'months is',current_savings,'.')
                                                    