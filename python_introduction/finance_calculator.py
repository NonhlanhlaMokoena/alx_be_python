#Personal Finance Calculator. This program calculates the user’s monthly savings based on inputted monthly income and expenses.

monthly_income = int(input("Enter your monthly income: "))
total_monthly_expenses = int(input("Enter your total monthly expenses: "))

simple_annual_interest = 0.05   #Simple annual interest rate is 5%     

monthly_savings = monthly_income - total_monthly_expenses

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print("Your monthly savings are", "$", monthly_savings)
print("Projected savings after one year, with interest, is:", "$", projected_savings, ".")
