# DAY 2

''' 
    EXERCISE 1
    
    BMI CALCULATOR
    
    height = 1.65
    weight = 84
    
    bmi = weight / height**2
    '''

# DAY 2 PROJECT

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_amount = int(input("How much tip would you like to give? 10, 12, or 15? "))
split_amount = int(input("How many people to split the bill? "))

payment = round((bill / split_amount) * ((tip_amount / 100) + 1), 2)
print("Each personn should pay: $" + str(payment)) 