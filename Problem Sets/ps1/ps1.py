#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 20:33:27 2017

@author: ksripinyo
"""

import numpy

annual_salary = float(input('What is your starting annual salary? '))
portion_down_payment= float(0.25) #defined by professor
portion_saved = float(input('What portion of your salary will you save each month (decimal form)? '))
total_cost = float(input('What is the total cost of your dream home? '))
current_savings = float(total_cost*portion_down_payment)
r = float(0.04) #The annual return rate on savings.
months = int(0) #set a variable for number of months

while current_savings < total_cost:
    current_savings = current_savings + current_savings*(r/12) + annual_salary*portion_saved
    print ('Savings at month',months,'=',round(current_savings,2))
    months = months +1

print ('Total months required to save for dream home:',months)
print ('Time required in years:',round(months/12,2))                                                    