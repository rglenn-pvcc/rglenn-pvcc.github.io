# Name: Robby Glenn
# Prog Purpose : this program generates receipts for purchasing plain pizza's at Palermo Pizza
# NOTES: All pizza are plain and come in four sizes small medium large and extralarge

#    Sales Tax 5.5%

##### User input ####
# Pizza size
# number of pizzas

#### Prices in USD ####
# Small 9.99
# Medium 12.99
# Large 14.99
# Extra Large 17.99
import datetime

########### Global variables
SALES_TAX_RATE = .055
SMALLZA = 9.99
MEDZA = 12.99
LARGEZA = 14.99
XLARGEZA = 17.99
SUBTOTAL = 0
TOTAL = 0
AMOUNTZA = 0
SALESTAXAMT = 0
#### Pizza size code
za_code = ""

def main():
    another_order=True
    while another_order:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like to place another order? (Y/N): ")
        if yesno == "n" or yesno == "N":
            another_order = False
            print("\n\t\tThank you for choosing Palermo Pizza")

def get_user_data():
    global AMOUNTZA, za_code
    za_code = str(input("Please choose your pizza size from small, medium, large, or extra large (S, M, L, X): "))
    AMOUNTZA = int(input("Please enter quantity: "))

def perform_calculations():
    global TOTAL, SUBTOTAL, SALES_TAX_RATE, SMALLZA, MEDZA, LARGEZA, XLARGEZA
    if za_code == "S" or za_code == "s":
        SUBTOTAL = AMOUNTZA * SMALLZA
    if za_code == "M" or za_code == "m":
        SUBTOTAL = AMOUNTZA * MEDZA
    if za_code == "L" or za_code == "l":
        SUBTOTAL = AMOUNTZA * LARGEZA
    if za_code == "X" or za_code == "x":
        SUBTOTAL = AMOUNTZA * XLARGEZA

    SALESTAXAMT = SUBTOTAL * SALES_TAX_RATE
    TOTAL = SUBTOTAL + SALESTAXAMT

def display_results():
    print('----------------------------------')
    print('State Sales Tax      $ ' + format(TOTAL - SUBTOTAL,'8,.2f'))
    print('Subtotal             $ ' + format(SUBTOTAL,'8,.2f'))
    print('Total                $ ' + format(TOTAL,'8,.2f'))
    print('----------------------------------')
    print(str(datetime.datetime.now()))
    

main()
