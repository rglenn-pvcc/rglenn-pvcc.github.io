# Name: Robby Glenn
# Prog Purpose: to convert temperature in celsius to fahrenheit

#define variables
c_temp = 0
f_temp = 0
last_name = "Glenn"
first_name = "Robby"

another_temp=True
while another_temp:
        c_temp= int(input("Enter the degress Celsius you want to convert: "))

        #calculate fahrenheit
        f_temp = (c_temp * 1.8) + 32

        #display results
        print("Celsius   : " + str(c_temp))
        print("Fahrenheit: " + str(f_temp))
        yesno = input("\nWould you like to convert another Celsius temperature? (Y/N: ")
        if yesno == "n" or yesno == "N":
            another_temp = False
        if yesno == "n" or yesno == "N":
            print("\n\t\tThank you for using this program :D")
            print("\n\t\tCheck out my webiste at rglenn-pvcc.github.io")
