startingSalary = int(input("Enter the starting salary: $"))
annualIncrease = float(input("Enter the annual % increase: ")) / 100
years = int(input("Enter the number of years: "))
print("Year\tSalary")
print("---------------")
for year in range(1, years + 1):
    startingSalary += startingSalary * annualIncrease
    print(f"{year}\t${startingSalary:,.2f}")

    #SHEEESH
