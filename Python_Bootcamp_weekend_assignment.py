# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#take input for marital status, ensuring it is either M or S
marital_status=input("Marital status(M for Married, S for Single): ")
while marital_status!="M" and marital_status!="S" :
    print("Invalid Marital Status, please enter M for married or S for Single: ")
    marital_status=input("Please enter correct Marital Status (M for Married, S for Single: ")
print(marital_status)

#Take input for labor rate, ensuring it is in numerical format

while True:
    try:
        wrate=float(input('Please enter hourly wages: '))
        break
    except ValueError:
        print("Invalid input. Wage rate must be in digits")

#Repeate above while loop for hours worked per month
while True:
    try:
        m_hrs=float(input('Please enter your average monthly work hours: '))
        break
    except ValueError:
        print("Invalid input. Hours worked must be in digits")
        
#Repeat loop for Bonus
while True:
    try:
        bonus=float(input('Please enter your annual bonus: '))
        break
    except ValueError:
        print("Invalid input. Bonus must be in numbers")
        
#Calculate Annual Gross Income
gross_income=(wrate*m_hrs)*12+bonus
print("")
print("ANNUAL GROSS INCOME: $", gross_income)

print("BEFORE TAX DEDUCTIONS")
#calculate before tax deductions
adj=0 #default value
print("\033[1m Adjustments(Medical, Parking Deduction, etc.): $", adj)
_401k=gross_income*0.1875 #Assumed default of 401k contributions
if _401k>20000: #cap 401k to 20k
    print("401K is capped to $20,000")
    _401k=20000
print("\033[1m 401K: $", _401k)
d_plus=0 #default value for dental plus
print("\033[1m Dental Plus: $",d_plus)
flexmed=0 #default value for flexmed
print("\033[1m Flexmed: $",flexmed)
_403b=0 #default value for 403b
print("\033[1m 403b (Catch Up): $", _403b)
bt_ded=adj+_401k+d_plus+flexmed+_403b
print("Total before Tax Adjustments: $", bt_ded)

#calculate taxable gross income
taxable_gross_income=gross_income-bt_ded

print("ANNUAL FEDERAL TAXABLE INCOME: $", taxable_gross_income)

#create function for getting the tax rate
def get_tax_slab(marital_status, taxable_gross_income):
    if marital_status=="S": #for single marital status
        if taxable_gross_income>0 and taxable_gross_income<=10275:
            tax_rate=0.10
        elif taxable_gross_income>10725 and taxable_gross_income<=41775:
            tax_rate=0.12
        elif taxable_gross_income>41775 and taxable_gross_income<=89075:
            tax_rate=0.22
        elif taxable_gross_income>89075 and taxable_gross_income<=170050:
            tax_rate=0.24
        elif taxable_gross_income>170050 and taxable_gross_income<=215950:
            tax_rate=0.32
        elif taxable_gross_income>215950 and taxable_gross_income<=539900:
            tax_rate=0.35
        elif taxable_gross_income>539901:
            tax_rate=0.37
    elif marital_status=="M": #for married status
        if taxable_gross_income>0 and taxable_gross_income<=20550:
            tax_rate=0.10
        elif taxable_gross_income>20550 and taxable_gross_income<=83550:
            tax_rate=0.12
        elif taxable_gross_income>83550 and taxable_gross_income<=178150:
            tax_rate=0.22
        elif taxable_gross_income>178150 and taxable_gross_income<=340100:
            tax_rate=0.24
        elif taxable_gross_income>340100 and taxable_gross_income<=431900:
            tax_rate=0.32
        elif taxable_gross_income>431900 and taxable_gross_income<=647850:
            tax_rate=0.35
        elif taxable_gross_income>647850:
            tax_rate=0.37
    return tax_rate

#perform wh tax calculation
wh_tax=get_tax_slab(marital_status,taxable_gross_income)*taxable_gross_income

#show annual witholding tax rate to user
tax_rate=str(100*get_tax_slab(marital_status, taxable_gross_income))

#Show tax calculations

print("Tax Rate:"+tax_rate+"%")
print("")
print("TOTAL TAXES")

W4_ex=0 #default value
print(" W4 Exemptions (Default): $", W4_ex)
print(" Federal Witholding tax: $", wh_tax)

fed_med=0.145*taxable_gross_income
print(" Fed MED/EE: $", fed_med)

#addl med calculation
if taxable_gross_income<=200000:
    addl_med=0
else:
    addl_med=taxable_gross_income*0.009
print(" Addl MED: $", addl_med)
fed_oasdi=0
print(" Fed OASDI/EE: $", fed_oasdi)

total_tax=wh_tax+W4_ex+fed_med+fed_oasdi+addl_med
print("Total Tax Amount: $", total_tax)

net_income=taxable_gross_income-total_tax
print("")
print("NET INCOME: $", net_income)
    
        

        