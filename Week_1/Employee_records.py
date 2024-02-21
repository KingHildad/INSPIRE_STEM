#get name,age,salary,bonuses,
#increase salary by 30%
#Decrease bonuses by 5000 ksh

Name=(input("Enter employee name:"))
Age=int(input("Enter employee age in years:"))
Salary=float(input("Enter employee salary:"))
Bonuses=float(input("Enter employee bonus:"))

New_salary=1.3*Salary
New_bonuses=Bonuses-int(5000)

print("The employee ",Name," is ",Age," years old and earns a salary of ",Salary, "plus bonuses worth ",Bonuses,)
print(Name,"New salary is ",New_salary," and his new bonus is ",New_bonuses)