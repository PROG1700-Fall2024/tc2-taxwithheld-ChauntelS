# Tax Withheld Calculator

# Write a console program that calculates the total amount of tax withheld from an employee’s weekly salary.
# The total withheld tax amount is calculated by combining the amount of provincial tax withheld and the amount of 
# federal tax withheld, minus a per-dependent deduction from the total tax withheld. The user will enter their pre-tax 
# weekly salary amount and the number of dependents they wish to claim. 
# 
# The program will calculate and output the amount of provincial tax withheld, amount of federal tax withheld, the 
# dependent tax deduction, and the user’s final take-home amount.
# Provincial withholding tax is calculated at 6.0%. Federal withholding tax is calculated at 25.0%. 
# The tax deduction for dependents is calculated at 2.0% of the employee’s salary per dependent.

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    # user input values 
    WeeklySalary = float(input("Enter your total weekly earnings:$"))
    NumberDepend = int(input("Enter number of dependents:"))

    #Variables
    ProvincialdW = float(0.06)
    FederalW = float(0.25)
    Dependents = float(0.02)

    PDeduct = float(WeeklySalary * ProvincialdW)
    FDeduct = float(WeeklySalary * FederalW)
    
    
    print("Total Provincial tax withheld:${0:.2f}".format(PDeduct))
    print("Total Federal taxwith held:${0:.2f}".format(FDeduct))
    
    TotalDuct = float((PDeduct) + (FDeduct))
    DDeduct = float((WeeklySalary) * (Dependents) * (NumberDepend))

    DDeduct = float((TotalDuct) * (Dependents) * int(NumberDepend))

    print("Total Dependent deduction for {0}".format(NumberDepend),"dependents:${0:.2f}" .format(DDeduct))

    TotalEarn = float((WeeklySalary - TotalDuct)+float(DDeduct))

    print("Total withheld:${0:.2f}".format(TotalDuct))

    print("Total take home:${0:.2f}".format(TotalEarn))

    # YOUR CODE ENDS HERE

main()
