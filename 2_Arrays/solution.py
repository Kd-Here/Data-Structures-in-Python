monthly_expense = [2200,2350,2600,2130,2190]
print("{} $ spent extra in Feb then Jan".format(monthly_expense[1]-monthly_expense[0]))

print("{} total expense in first quarter".format(sum(monthly_expense[:3])))

if 2000 in monthly_expense:
    print("Yes spend exactly 2000$")

monthly_expense.append(1980)

monthly_expense[3] =  monthly_expense[3]-200

print(monthly_expense)