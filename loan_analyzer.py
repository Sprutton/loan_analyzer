# coding: utf-8
import csv
from pathlib import Path
loan_costs = [500, 600, 200, 1000, 450]
loan_count = len(loan_costs)
loan_total = sum(loan_costs)
avg_loan = loan_total/loan_count

print("\nPart One:\n")
print(f"Loan Count: {loan_count}\nLoan Total: {loan_total}\nAverage Loan: {avg_loan}")
print(
    f"The total number of loans is {loan_count}, the total cost of loans given is ${float(loan_total)} and the average loan given is ${avg_loan}.")

print("\nPart Two:\n")
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

remaining_months = loan.get("remaining_months")
future_value = loan.get("future_value")
print(f"Remaining Months: {remaining_months}\nFuture Value: {future_value}")
present_value = future_value / (1 + .20 / 12) ** remaining_months
print(f"Present Value: ${round(present_value,2)}")

if present_value >= present_value:
    print("The loan is at worth at least the cost to buy it.")
else:
    print("The loan is too expensive and not worth the price.")
print("\nPart Three:\n")
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}


def present_value(future_value, remaining_months, annual_discount_rate):
    present_value = round(
        future_value / (1 + annual_discount_rate / 12) ** remaining_months, 2)
    return(present_value)


annual_discount_rate = 0.2
present_value = present_value(new_loan.get('future_value'), new_loan.get(
    'remaining_months'), annual_discount_rate)
print(f"The present value of the loan is: {present_value}\n")
print("Part Four: ")
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]
inexpensive_loans = []
for i in loans:
    if i["loan_price"] <= 500:
        inexpensive_loans.append(i)
print("\nInexpensive Loans:")
for i in inexpensive_loans:
    print(i)

header = ["loan_price", "remaining_months",
          "repayment_interval", "future_value"]
output_path = Path("inexpensive_loans.csv")
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    for row in inexpensive_loans:
        csvwriter.writerow(row.values())
