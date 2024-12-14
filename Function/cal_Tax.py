def calculate_tax(income):
    tax = 0
    
    if income <= 250000:
        tax = 0
    elif income <= 500000: 
        tax = (income - 250000) * 0.05
    elif income <= 1000000:
        tax = (500000 - 250000) * 0.05 + (income - 500000) * 0.20
    else:
        tax = (500000 - 250000) *0.05 + (1000000 - 500000) * 0.20 + (income - 1000000) * 0.30

    return tax

income = int(input("Enter Income:->"))

tax = calculate_tax(income)

print(f"Income is {income} and payable tax is {tax}")