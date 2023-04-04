# Name: Adela Cervantes
# Name: Robby Glenn
# Prog Purpose: Find the gross pay, deductions, and net pay for an employee based
####### on the number of hours they worked and their job category.

# define tax rate and job category pay rates
# C Cashier pay rate = $16.50
# S Stocker pay rate = $15.75
# J Janitor pay rate = $15.75
# M Maintenance pay rate = $19.50
###### Tax rates ####
# Federal tax rate = .12
# State income tax rate = .03
# social security rax rate = .062
# Medicare tax rate = .0145

import datetime

######### define global variables
FEDERAL_TAX_RATE = .12
STATE_INCOME_TAX_RATE = .03
SOCIAL_SECURITY_TAX_RATE = .062
MEDICARE_TAX_RATE = .0145
#### PR = pay rate
CPR = 16.50
SPR = 15.75
JPR = 15.75
MPR = 19.50
#### job code
job_code = ""

##### define global variables 
netpay = 0
grosspay = 0
#### variable AMT for tax rates
fedtaxamt = 0
statetaxamt = 0
socialtaxamt = 0
medicaretaxamt = 0
hoursworked = 0
totaldeductions = 0


############define program functions 
def main():
    another_emp=True
    while another_emp:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like to check another Employee? (Y/N): ")
        if yesno == "n" or yesno == "N":
            another_emp = False
            print("\n\t\tThank you for using this program :D")
            print("\n\t\tCheck out my webiste at rglenn-pvcc.github.io")   

def get_user_data():
    global job_code, hoursworked
    job_code = str(input("Job Category Code (C, S, J, M): "))
    hoursworked = int(input("Hours worked: "))

def perform_calculations():
    global grosspay, deductions, netpay, totaldeductions, fedtaxamt, statetaxamt, socialtaxamt, medicaretaxamt
    if job_code == "C" or job_code == "c":
        grosspay = hoursworked * CPR
    if job_code == "S" or job_code == "s":
        grosspay = hoursworked * CPR
    if job_code == "J" or job_code == "j":
        grosspay = hoursworked * CPR
    if job_code == "M" or job_code == "m":
        grosspay = hoursworked * CPR
    
    fedtaxamt = grosspay * FEDERAL_TAX_RATE
    statetaxamt = grosspay * STATE_INCOME_TAX_RATE
    socialtaxamt = grosspay * SOCIAL_SECURITY_TAX_RATE
    medicaretaxamt = grosspay * MEDICARE_TAX_RATE
    totaldeductions = fedtaxamt + statetaxamt + socialtaxamt + medicaretaxamt
    netpay = grosspay - totaldeductions
    
##### results - deduction amts, gross, and net
    
def display_results():
    print('----------------------------------')
    print('Social Tax Deduction  $ ' + format(socialtaxamt,'8,.2f'))
    print('State Tax Deduction   $ ' + format(statetaxamt,'8,.2f'))
    print('Federal Tax Deduction $ ' + format(fedtaxamt,'8,.2f'))
    print('Gross Pay             $ ' + format(grosspay,'8,.2f'))
    print('Total Deductions      $ ' + format(totaldeductions,'8,.2f'))
    print('Net Pay               $ ' + format(netpay,'8,.2f'))
    print('----------------------------------')
    print(str(datetime.datetime.now()))
    

main()
