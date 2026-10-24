# Electricity Billing System 
def calculate_bill(units): 
    if units <= 100: 
        return units * 1.50 
    elif units <= 200: 
        return (100 * 1.50) + (units - 100) * 2.50 
    elif units <= 500: 
        return (100 * 1.50) + (100 * 2.50) + (units - 200) * 4.00 
    else: 
        return (100 * 1.50) + (100 * 2.50) + (300 * 4.00) + (units - 500) * 6.00 

n = int(input("Enter number of customers: ")) 

for i in range(1, n + 1): 
    print(f"\nCustomer {i}") 
    name = input("Enter customer name: ") 
    units = float(input("Enter units consumed: ")) 
    
    while units < 0:
        print("Invalid input! Units cannot be negative.")
        units = float(input("Enter valid units consumed: "))
        
    bill = calculate_bill(units)
    
    print("Customer Name :", name) 
    print("Units :", units) 
    print("Bill Amount : Rs.", round(bill, 2))