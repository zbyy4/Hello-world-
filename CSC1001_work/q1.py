final_value = eval(input("Enter the final account value: "))
annual_rate = eval(input("Enter the annual interest rate: "))/100
years = eval(input("Enter the number of years: "))
initial_deposit = final_value/(1+annual_rate)**years
print("The initial value is: ", initial_deposit)